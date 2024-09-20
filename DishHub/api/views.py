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
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth import get_user_model


User= get_user_model()
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
    def post(self, request):
        email = request.data.get('username')
        password = request.data.get('password')
        print(f"$$$${email}$$$$$$$$$$$$$$$$$$$$$$$$$$$$${password}$$$$$$$$$")
        
        user = authenticate(request, username=email, password=password)
        if user is not None:
            print("*********************************")
            refresh = RefreshToken.for_user(user)
            return Response({
                 "Login successful! Welcome back!",
            }, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)



class UserProfileUpdateView(APIView):
    def get_object(self, pk):
        return User.objects.get(pk=pk)

    def get(self, request):
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

    def patch(self, request, pk):
        model = self.get_object(pk)
        serializer = UserSerializer(model, data=request.data, partial=True)
        if serializer.is_valid():
            user = serializer.save()
            logger.info(f'User profile updated successfully: {user.email}')
            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.error(f'User profile update failed for {request.user.email}: {serializer.errors}')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserListView(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
class UserListView(APIView):
    
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class UserDetailView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

def generate_token(request):
    user,created =User.objects.get_or_create(username=' ')
    refresh = RefreshToken.for_user(user)
    return JsonResponse({
        'access':str(refresh.access_token),
        'refresh':str(refresh)
})