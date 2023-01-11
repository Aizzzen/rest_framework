"""drfsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from women.views import *
from rest_framework import routers

# создание простого роутера
router = routers.SimpleRouter()
router.register(r'women', WomenViewSet)

# при использовании Viewset можно передавать параметры
# метод для обработки запроса и метод, который вызывается во viewset-е для обработки этого запроса
# list update - названия стандартных методов
urlpatterns = [
    path('admin/', admin.site.urls),
    # пропишем набор автоматически сгенерированных маршрутов
    path('api/v1/', include(router.urls))   # http://127.0.0.1:8000/api/v1/women

    # path('api/v1/womenlist/', WomenViewSet.as_view({'get': 'list'})),
    # path('api/v1/womenlist/<int:pk>', WomenViewSet.as_view({'put': 'update'})),
]
