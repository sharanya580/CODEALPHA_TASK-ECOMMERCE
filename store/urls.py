from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('product/<str:pk>/', views.product_detail, name="product"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
]
