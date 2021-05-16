from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

app_name = 'cart'

urlpatterns = [
    path('cart/<int:pk>/', views.CartDetailView.as_view(), name = 'detail'),
]