from rest_framework import generics, viewsets

from .models import Women
from .serializers import WomenSerializer


class WomenViewSet(viewsets.ModelViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

# 1 класс ViewSet заменяет 3 вышеперечисленных класса
