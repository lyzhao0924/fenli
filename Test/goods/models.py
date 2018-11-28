from django.db import models

# Create your models here.
class Goods(models.Model):
    name = models.CharField(max_length=11,verbose_name="商品名称")


    class Meta:
        verbose_name = "商品信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
