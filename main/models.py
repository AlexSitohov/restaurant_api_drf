from django.contrib.auth.models import User
from django.db.models import *


class Restaurant(Model):
    title = CharField(max_length=100)
    opening_year = PositiveIntegerField()
    city = CharField(max_length=100)
    street = CharField(max_length=100)
    rating = PositiveIntegerField(default=0)
    balance = DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.pk} {self.title}'


class Worker(Model):
    restaurant = ForeignKey(Restaurant, related_name='workers', on_delete=CASCADE, null=True, blank=True)
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    age = PositiveIntegerField()
    experience = PositiveIntegerField()

    Choices = (
        (1, 'cook'),
        (2, 'waiter'),
        (3, 'administrator')
    )

    position = IntegerField(choices=Choices)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.position}'


class Dish(Model):
    restaurant = ForeignKey(Restaurant, related_name='dishes', on_delete=CASCADE, null=True, blank=True)
    title = CharField(max_length=100)
    description = TextField()
    price = DecimalField(max_digits=6, decimal_places=2)
    weight = PositiveIntegerField()

    def __str__(self):
        return f'{self.title} {self.restaurant}'


class Order(Model):
    client = ForeignKey('Customer', on_delete=CASCADE)
    restaurant = ForeignKey(Restaurant, related_name='orders', on_delete=CASCADE, null=True, blank=True)
    dish = ManyToManyField(Dish)
    officiant = ForeignKey(Worker, on_delete=CASCADE)
    order_time = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.pk}.{self.client} - {self.dish}'


class Customer(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    balance = DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'customer - {self.user}'
