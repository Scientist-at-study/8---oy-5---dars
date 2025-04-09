from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=150, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    photo = models.ImageField(upload_to="product/photos", null=True, blank=True)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    date_of_ordering = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}, phone: {self.phone_number}"


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=40, null=True, blank=True)
    delivery = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Order {self.id} by {self.client.name}"
