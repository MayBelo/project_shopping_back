from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    # quantity = models.IntegerField(null=True,blank=True, default=0)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    image = models.ImageField(null=True, blank=True,
                              default='/placeholder.png')

                              
    def __str__(self):
        return self.name
# class Cart(models.Model):
#     name = models.CharField(max_length=200)
#     created = models.DateField(auto_now_add=True)
#     updated = models.DateField(auto_now=True)

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product")
    quantity = models.IntegerField(null=False, default=1)
    in_cart = models.BooleanField(default=False,)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.product.name