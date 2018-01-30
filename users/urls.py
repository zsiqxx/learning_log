"""定义users的URL模式"""

from django.urls import path,re_path
from django.contrib.auth.views import login

from . import views

urlpatterns = [
        #登录页面
        re_path('^login/$',login,{'template_name':'users/login.html'},name='login'),

        #注销
        re_path('^logout/$',views.logout_view,name='logout'),

        #注册
        re_path('^register/$',views.register,name='register'),
]

app_name = 'users'
