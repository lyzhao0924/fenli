"""Test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
# from django.contrib import admin
from rest_framework import routers

from user import views
from user.views import index

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
from goods import views
router.register(r'goods', views.GoodsViewSet)

import xadmin

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^user/',include('user.urls',namespace='user')),
    url(r'^goods/',include('goods.urls',namespace='goods')),
    url(r'^json', index),

]
