from django.urls import path
from . import views
from .views import login_view, logout_view, product_detail

urlpatterns = [
    path('', views.register, name='register'),
     path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('home/', views.home, name='home'),
    path('product/', views.product_list, name='product_list'),
    path('products/<slug:slug>/', product_detail, name='product_detail'),


]
