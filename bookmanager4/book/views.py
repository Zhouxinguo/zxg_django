
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.http import JsonResponse



def creates(request):

    return HttpResponse('周某人')

def shop(request):
    query_params = request.GET
    order = query_params.get('order')
    print(order)
    return HttpResponse('周哥的小公司')

def goods(request,cat_id,mobile):

    return JsonResponse({'cat_id':cat_id,'good_id':mobile})

def register(request):
    data = request.POST
    print(data)
    return HttpResponse('ok')

def json(request):
    body = request.body
    print(body)

    # 转换为字符串
    body_str = body.decode()
    print(body_str)

    # 转换为字典
    import json
    body_dict = json.loads(body_str)
    print(body_dict)

    ######## 请求头 ###########
    print(request.META)
    print(request.META['SERVER_PORT'])

    return HttpResponse('json')

def method(request):
    # 查看当前请求方式
    print(request.method)

    return HttpResponse('okk')


def response(request):
    response = HttpResponse('res',status=200)

    response['name'] = 'zhouxinguo'

    return response

def jsonres(request):

    info = [
        {
            'name': 'zhouxinguo',
            'address': 'changde'
        },
        {
            'name':'zxg',
            'address':'xiangtan'
        }
    ]

    response = JsonResponse(data=info,safe=False)

    return response

from django.shortcuts import redirect
def baidu(request):
    return redirect('https://www.baidu.com')


######### Cookie ###############
def set_cookie(request):

    # 1.获取查询字符串数据
    username = request.GET.get('username')
    password = request.GET.get('password')
    # 2.服务器设置cookie信息
    # 通过响应对象.set_cookie 方法
    response = HttpResponse('set_cookie')
    # key,value=''
    response.set_cookie('name',username)
    response.set_cookie('password',password,max_age=3600)

    response.delete_cookie('name')

    return response

def get_cookie(request):

    # 获取cookie
    print(request.COOKIES)
    name = request.COOKIES.get('name')

    return HttpResponse(name)



############## Session ##############

def set_session(request):

    # 1.模拟 获取用户信息
    username = request.GET.get('username')

    # 2.设置session信息
    user_id = 1

    request.session['user_id'] = user_id
    request.session['username'] = username
    return HttpResponse('set_session')

def get_session(request):

    user_id = request.session.get('user_id')
    username = request.session.get('username')

    content = '{},{}'.format(user_id,username)
    return HttpResponse(content)







########### 类视图 #############
from django.views.generic import View

class LoginView(View):

    def get(self,request):
        return HttpResponse('GET GET GET')

    def post(self,request):
        return HttpResponse('POST POST POST')


from django.contrib.auth.mixins import LoginRequiredMixin
class OrderView(LoginRequiredMixin,View):
    def get(self,request):

        return HttpResponse('GET 我的订单页面,这个页面必须登录')

    def post(self,request):
        return HttpResponse('POST 我的订单页面,这个页面必须登录')
