from django.urls import path
from book.views import creates,goods,shop,register
from book.views import json,method,response
from book.views import jsonres,baidu,set_cookie,get_cookie
from book.views import set_session,get_session
from book.views import LoginView,OrderView

from django.urls import converters
from django.urls.converters import register_converter

# 1.定义转换器
class MobileConverter:
    regex = '1[3-9]\d{9}'

    def to_python(self, value):
        return value

    # def to_url(self, value):
    #     return str(value)
# 2. 先注册转换器,才能在第三步使用
register_converter(MobileConverter,'phone')

urlpatterns = [
    path('create/',creates),
    path('11000/11005/',shop),
    path('<int:cat_id>/<phone:mobile>/', goods),
    path('register/',register),
    path('json/',json),
    path('method/',method),
    path('res/',response),
    path('jsres/',jsonres),
    path('baidu/',baidu),
    path('set_cookie/',set_cookie),
    path('get_cookie/',get_cookie),
    path('set_session/', set_session),
    path('get_session/', get_session),

    path('login/',LoginView.as_view()),
    path('order/',OrderView.as_view()),
]