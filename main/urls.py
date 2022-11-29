from django.urls import path, include
from rest_framework.routers import *

from main.api import *

router = SimpleRouter()
router.register('restaurant', RestaurantAPI)
router.register('worker', WorkerAPI)
router.register('dish', DishAPI)


urlpatterns = [
    path('api/', include(router.urls)),
    path('api/restaurants/', RestaurantAPIView.as_view()),
    path('api/restaurants/<int:pk>/', RestaurantInstanceAPIView.as_view()),
    path('api/workers/', WorkersAPIView.as_view()),
    path('api/workers/<int:pk>/', WorkerAPIView.as_view()),
    path('api/rate_restaurant/', RateRestaurants.as_view()),
    path('api/order/',OrderAPI.as_view())

]
