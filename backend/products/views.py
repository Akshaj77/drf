from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        #serializer.save(user = self.request.user) 
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title

        serializer.save(content = content)
        # send a Django signal


class ProductListAPIView(generics.ListAPIView):
    '''
    Not gonna use
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer




class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



    