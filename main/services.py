from django.db import transaction

from main.models import *


def rate_restaurant(restaurant, ball):
    with transaction.atomic():
        restaurant.rating = restaurant.rating + ball
        restaurant.save()


def payment(serializer):
    pk_dish = serializer.data.get('dish')
    dish = Dish.objects.get(pk=pk_dish)
    payment_value = dish.price
    pk_client = serializer.data.get('client')
    client = Customer.objects.get(pk=pk_client)
    pk_restaurant = serializer.data.get('restaurant')
    restaurant = Restaurant.objects.get(pk=pk_restaurant)
    client.balance -= payment_value
    restaurant.balance += payment_value
    client.save()
    restaurant.save()
