from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ValidationError
from shopping.models import Shopping_list, Shopping_list_item
from .serializers import ShoppingListSerializer, ShoppingListItemSerializer

class ShoppingListList(generics.ListCreateAPIView):
    queryset = Shopping_list.objects.all()
    serializer_class = ShoppingListSerializer

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except ValidationError as ve:
            return Response({"error": ve.detail}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)





class ShoppingListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shopping_list.objects.all()
    serializer_class = ShoppingListSerializer

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except NotFound:
            return Response({"error": "Shopping list not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        try:
            return super().put(request, *args, **kwargs)
        except ValidationError as ve:
            return Response({"error": ve.detail}, status=status.HTTP_400_BAD_REQUEST)
        except NotFound:
            return Response({"error": "Shopping list not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            shopping_list = self.get_object()  
            self.perform_destroy(shopping_list)  
            return Response(
                {"message": "Shopping list deleted successfully.", "deleted_item": self.serializer_class(shopping_list).data},
                status=status.HTTP_200_OK 
            )
        except NotFound:
            return Response({"error": "Shopping list not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)








class ShoppingListItemList(generics.ListCreateAPIView):
    queryset = Shopping_list_item.objects.all()
    serializer_class = ShoppingListItemSerializer

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except ValidationError as ve:
            return Response({"error": ve.detail}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)









class ShoppingListItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shopping_list_item.objects.all()
    serializer_class = ShoppingListItemSerializer

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except NotFound:
            return Response({"error": "Shopping list item not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        try:
            return super().put(request, *args, **kwargs)
        except ValidationError as ve:
            return Response({"error": ve.detail}, status=status.HTTP_400_BAD_REQUEST)
        except NotFound:
            return Response({"error": "Shopping list item not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            shopping_list_item = self.get_object()  
            self.perform_destroy(shopping_list_item)  
            return Response(
                {"message": "Shopping list item deleted successfully.", "deleted_item": self.serializer_class(shopping_list_item).data},
                status=status.HTTP_200_OK  
            )
        except NotFound:
            return Response({"error": "Shopping list item not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)