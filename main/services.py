from django.db import transaction
from rest_framework import exceptions

from main.models import *


def rate_restaurant(restaurant, ball):
    with transaction.atomic():
        restaurant.rating = restaurant.rating + ball
        restaurant.save()


def payment(serializer):
    payment_value = 0
    dishes = serializer.data.get('dish')
    for dish in dishes:
        meal = Dish.objects.get(pk=dish)
        payment_value += meal.price
    pk_client = serializer.data.get('client')
    client = Customer.objects.get(pk=pk_client)
    pk_restaurant = serializer.data.get('restaurant')
    restaurant = Restaurant.objects.get(pk=pk_restaurant)
    client.balance -= payment_value
    if client.balance < 0:
        return 1
    restaurant.balance += payment_value
    client.save()
    restaurant.save()
