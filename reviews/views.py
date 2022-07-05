from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import ProductSerializer
from .models import Product
from rest_framework.decorators import action

class ProductViewSet(ReadOnlyModelViewSet):

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    
    @action(detail=False)
    def get_list(self, request):
        pass
      
    @action(detail=True)
    def get_product(self, request, pk=None):
        pass

    @action(detail=True, methods=['post', 'delete'])
    def delete_product(self, request, pk=None):
        pass