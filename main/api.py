from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.generics import *

from main.models import *
from main.permissions import IsAdminOrReadOnly
from main.serializers import *
from main.services import rate_restaurant, payment


# mixins.CreateModelMixin,
# mixins.RetrieveModelMixin,
# mixins.UpdateModelMixin,
# mixins.DestroyModelMixin,
# mixins.ListModelMixin,
# GenericViewSet


class RestaurantAPI(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAdminOrReadOnly]


class RestaurantAPIView(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request):
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = RestaurantSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


class RestaurantInstanceAPIView(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request, pk):
        restaurant = Restaurant.objects.get(pk=pk)
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data)

    def delete(self, request, pk):
        restaurant = Restaurant.objects.get(pk=pk)
        restaurant.delete()
        return Response({'msg': 'deleted'})

    def put(self, request, pk, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        restaurant = Restaurant.objects.get(pk=pk)
        serializer = RestaurantSerializer(restaurant, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(restaurant, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the restaurant.
            restaurant._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


class WorkerAPI(ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    permission_classes = [IsAdminOrReadOnly]


class WorkerAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    permission_classes = [IsAdminOrReadOnly]


class WorkersAPIView(ListCreateAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    permission_classes = [IsAdminOrReadOnly]


class DishAPI(ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [IsAdminOrReadOnly]


class RateRestaurants(APIView):
    def post(self, request):
        data = request.data
        pk_restaurant_to_rate = data.get('restaurant')
        restaurant = Restaurant.objects.get(pk=pk_restaurant_to_rate)
        ball = data.get('ball')
        rate_restaurant(restaurant, ball)

        return Response(RestaurantSerializer(restaurant).data)


class OrderAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = OrderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            if payment(serializer) == 1:
                return Response({'msg': "3243"})

            # payment(serializer)

            return Response(serializer.data)


#
# class OrderAPI(ListCreateAPIView):
#     queryset= Order.objects.all()
#     serializer_class = OrderSerializer


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
