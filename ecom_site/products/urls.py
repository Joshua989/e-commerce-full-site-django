from django.urls import path
from . import views
from .views import login_view, logout_view, product_detail, cart_view, add_to_cart, remove_from_cart, update_cart, wishlist_view, add_to_wishlist, remove_from_wishlist

urlpatterns = [
    path('', views.register, name='register'),
     path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('home/', views.home, name='home'),
    path('product/', views.product_list, name='product_list'),
    path('products/<slug:slug>/', product_detail, name='product_detail'),
    path('cart/', cart_view, name='cart_view'),
    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('cart/update/<int:item_id>/', update_cart, name='update_cart'),
      path('wishlist/', wishlist_view, name='wishlist_view'),
    path('wishlist/add/<int:product_id>/', add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<int:product_id>/', remove_from_wishlist, name='remove_from_wishlist'),



]
