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



"""class orders(models.Model):
    fullname = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.fullname}  {self.address}"""

class Order(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='pending')
    payment_status = models.CharField(max_length=20, default='pending')  # pending, paid, failed
    payment_method = models.CharField(max_length=50, blank=True, null=True)
    paid_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Order {self.id} by {self.full_name}"


