from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from apps.shop.models import Product



class ProductListView(ListView):
    template_name = "product_list.html"
    model = Product
    queryset = Product.objects.filter(is_available = True)

class DetailProductView(DetailView):
    template_name="detail_product.html"
    model = Product

