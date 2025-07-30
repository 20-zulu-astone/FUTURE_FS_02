from django.db import models

class products(models.Model):
    name = models.CharField(max_length=30)
    price = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField(default = 0)
    description = models.TextField()
    product_image = models.ImageField(upload_to = 'product_images/')

    def __str__(self):
        return f"{self.name}  - {self.price} {self.product_image}"



class cartitem(models.Model):
    product = models.ForeignKey(products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def subtotal(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product



class orders(models.Model):
    fullname = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.fullname}  {self.address}"

