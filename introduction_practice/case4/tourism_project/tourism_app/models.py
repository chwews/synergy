from django.db import models

class Tour(models.Model):
    tour_name = models.CharField(max_length=255)
    tour_description = models.TextField()
    duration = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Service(models.Model):
    service_name = models.CharField(max_length=255)
    service_description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Client(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

class Operator(models.Model):
    operator_name = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE)
    order_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
