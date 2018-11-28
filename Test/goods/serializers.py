from rest_framework import serializers

from goods.models import Goods


class GoodsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Goods
        fields = ['name']