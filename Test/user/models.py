from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=10,verbose_name='名字')
    email = models.EmailField(max_length=20,verbose_name='邮箱')


    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username