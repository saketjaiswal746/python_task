
from django.urls import path
from .views import product_list_view, ProductListCreate, ProductRetrieveUpdateDestroy, TopProductsAPIView

urlpatterns = [
    path('', product_list_view, name='product-list-view'),  # This is the root URL pattern
    path('api/products/', ProductListCreate.as_view(), name='product-list-create'),
    path('api/products/<int:pk>/', ProductRetrieveUpdateDestroy.as_view(), name='product-detail'),
    path('api/products/top/<str:time_range>/', TopProductsAPIView.as_view(), name='top-products'),
]
