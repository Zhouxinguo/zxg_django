############ 定义中间件 ###########
from django.utils.deprecation import MiddlewareMixin


class TestMiddleware1(MiddlewareMixin):

    def process_request(self, request):
        print('process_request1 被调用')

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('process_view1 被调用')

    def process_response(self, request, response):
        print('process_response1 被调用')
        return response


class TestMiddleware2(MiddlewareMixin):
    def process_request(self,request):
        print('process_request2 被调用')

    def peocess_view(self,request,view_func,view_args,view_kwargs):
        print('process_view2 被调用')

    def process_response(self,request,response):
        print('process_response2 被调用')
        return response