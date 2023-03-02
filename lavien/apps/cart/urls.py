from django.urls import path
from . import views

urlpatterns=[
    path('', views.CartPage.as_view(), name = "cart_page"), 
    path('add/<int:product_id>/', views.AddCartView.as_view(), name="add_cart"),
    path('delete/<int:product_id>/', views.DeleteProductCart.as_view(), name="delete_cart"), 
    

]