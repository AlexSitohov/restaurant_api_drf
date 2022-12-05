from rest_framework.serializers import *

from main.models import *


class RestaurantSerializer(ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'title', 'opening_year', 'city', 'street', 'rating', 'workers', 'dishes', 'balance']
        read_only_fields = ['rating', 'workers', 'dishes', 'balance']


class WorkerSerializer(ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'


class DishSerializer(ModelSerializer):
    class Meta:
        model = Dish
        fields = '__all__'


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
