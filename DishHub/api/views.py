from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.tokens import RefreshToken
from users.models import User
from .serializers import UserSerializer, LoginSerializer
import json
import logging

logger = logging.getLogger(__name__)

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            logger.info(f'User registered successfully: {user.email}')
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        
        logger.error(f'User registration failed: {serializer.errors}')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        users = User.objects.all()  
        serializer = UserSerializer(users, many=True)  
        logger.info('Fetched user details successfully.')
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    

class LoginView(APIView):
    permission_classes = [AllowAny]         

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        
        if not email or not password:
            return Response({'error': _('Email and password are required')}, status=status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(username=email, password=password)
        if user:
            logger.info(f'User logged in successfully: {email}')
            return Response({}, status=status.HTTP_200_OK)

        logger.error(f'Login failed for user: {email}')
        return Response({'error': _('Invalid credentials')}, status=status.HTTP_401_UNAUTHORIZED)
    
    def get(self, request):
        return Response({
            'message': _('This endpoint allows users to log in using their email and password.'),
            'usage': _('Send a POST request with "email" and "password" fields to log in.')
        }, status=status.HTTP_200_OK)
        
        

logger = logging.getLogger(__name__)

class UserProfileUpdateView(APIView):
    permission_classes = []  

    def get(self, request):
        if not request.user.is_authenticated:
            logger.warning('Attempt to retrieve profile by unauthenticated user.')
            return Response({"detail": "Unauthorized access. Please log in."}, status=status.HTTP_401_UNAUTHORIZED)

        user = request.user
        serializer = UserSerializer(user)
        logger.info(f'User profile retrieved successfully: {user.email}')
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data=request.data, instance=request.user)
        if serializer.is_valid():
            user = serializer.save()
            logger.info(f'User profile updated successfully: {user.email}')
            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.error(f'User profile update failed: {serializer.errors}')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            user = serializer.save()
            logger.info(f'User profile updated successfully: {user.email}')
            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.error(f'User profile update failed for {request.user.email}: {serializer.errors}')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
class UserListView(APIView):
    
    permission_classes = [IsAuthenticated]
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class UserDetailView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

@csrf_exempt
def generate_token(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')

            if not email:
                return JsonResponse({'error': 'Email is required'}, status=400)

            user, created = User.objects.get_or_create(email=email)

            if created:
                user.set_password('default_password')  # Set a default password if needed
                user.save()

            refresh = RefreshToken.for_user(user)

            return JsonResponse({
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            })
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    return JsonResponse({'error': 'Method not allowed'}, status=405)
