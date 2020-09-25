from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from book.models import BookInfo
# 数据库操作:增
def creates(request):
    BookInfo.objects.create(
        name = '周新国',
        pub_date = '2001-1-1'
    )

    return HttpResponse('周某人')

# 数据库操作:改
from book.models import PeopleInfo
person = PeopleInfo.objects.get(name='郭靖')
person.name = '周新国'
person.save()

PeopleInfo.objects.filter(name= '周新国').update(name='郭靖')


# 数据库操作:删除
person = PeopleInfo.objects.get(name='郭靖')
person.delete()


BookInfo.objects.filter(name='周新国').delete()