from django.urls import path

from apps.shop import views


urlpatterns = [
    path("product/list/", views.ProductListView.as_view(), name= "product_list"), 
    path("detail/product/<int:pk>/", views.DetailProductView.as_view(), name="deatail_product"),
]