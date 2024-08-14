from django.shortcuts import render

# Create your views.


from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count  # Import Count
from django.utils import timezone
from datetime import timedelta
from .models import Product
from .serializers import ProductSerializer

def product_list_view(request):
    return render(request, 'product_list.html')

class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class TopProductsAPIView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        time_range = kwargs.get('time_range', 'all')
        now = timezone.now()

        if time_range == 'all':
            products = Product.objects.all()
        elif time_range == 'last_day':
            start_time = now - timedelta(days=1)
            products = Product.objects.filter(retrieved_at__gte=start_time)
        elif time_range == 'last_week':
            start_time = now - timedelta(weeks=1)
            products = Product.objects.filter(retrieved_at__gte=start_time)
        else:
            return Response({'error': 'Invalid time range'}, status=status.HTTP_400_BAD_REQUEST)

        product_counts = products.values('title', 'description', 'price').annotate(count=Count('id')).order_by('-count')[:5]
        return Response(product_counts)
    
