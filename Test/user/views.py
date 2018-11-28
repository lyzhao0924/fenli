from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from rest_framework import viewsets

from user.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


import json

from django.http import HttpResponse

def index(request):
    data = {}
    data['remote_addr(请求的ip)'] = request.META.get('REMOTE_ADDR')
    data['User-agent(请求头)'] = request.META.get('HTTP_USER_AGENT')
    data['Referer(跳转处)'] = request.META.get('HTTP_REFERER')
    data['Cookie(令牌)'] = request.META.get('HTTP_COOKIE')
    data['Method(请求方法)'] = request.method
    json_content = json.dumps(data, ensure_ascii=False)
    return HttpResponse(json_content, content_type='application/json', charset='utf-8')
