from django.contrib.auth.models import User
from rest_framework import serializers

#超链接关系HyperlinkedModelSerializer
class UserSerializer(serializers.HyperlinkedModelSerializer,):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', )


