from django.db import models

# Create your models here.

from apps.blog.models import Organization

class ShopCategory(models.Model):
    name = models.CharField("Название", max_length=50)
    slug = models.SlugField(max_length=70)

    class Meta:
        verbose_name = "Категория товара"
        verbose_name_plural = "Категрии товара"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField("Название", max_length=255)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        ShopCategory, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name="products"
    )
    is_available = models.BooleanField("Доступно", default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField("Фото", upload_to="product/images/", null=True)
    organization = models.ForeignKey(Organization, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name="products")



    class Meta:
   
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["-created"]

    def __str__(self):
        return self.name



    