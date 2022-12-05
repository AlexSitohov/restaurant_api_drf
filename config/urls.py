from django.contrib import admin
from django.urls import path, include
from main.yasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('drf-auth/', include('rest_framework.urls'))
]

urlpatterns += doc_urls
