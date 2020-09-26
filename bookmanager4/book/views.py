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



