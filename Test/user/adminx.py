import xadmin
#定义任意一个类：model名字+Admin
from user.models import User


class UserAdmin(object):
	#后台显示丰富一下
	list_display = ["username","email",]


#第一个参数是modle,第二个参数是，VerifyCodeAdmin
xadmin.site.register(User,UserAdmin)