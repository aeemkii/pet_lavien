from django.shortcuts import render, redirect

# Create your views here.

from django.views.generic import TemplateView
from django.views import View
from .cart import Cart

from apps.shop.models import Product

class CartPage(TemplateView):
    template_name = "cart.html"


class AddCartView(View):


    def get(self, request, product_id):
        cart = Cart(request)
        product = Product.objects.get(id=product_id)
        cart.add(
            product = product, 
            quantity = 1
        )
        return redirect("cart_page")


class DeleteProductCart(View):
    def get(self, request, product_id):

        cart = Cart(request)
        product = Product.objects.get(id=product_id)
        cart.remove(product)
        return redirect("cart_page")
