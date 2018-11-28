from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from goods.models import Goods
from goods.serializers import GoodsSerializer


class GoodsViewSet(viewsets.ModelViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
