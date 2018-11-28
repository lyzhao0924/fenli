import xadmin
#定义任意一个类：model名字+Admin
from goods.models import Goods


class GoodsAdmin(object):
	#后台显示丰富一下
	list_display = ["name",]


#第一个参数是modle,第二个参数是，VerifyCodeAdmin
xadmin.site.register(Goods,GoodsAdmin)