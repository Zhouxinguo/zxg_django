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
# from book.models import PeopleInfo
# person = PeopleInfo.objects.get(name='郭靖')
# person.name = '周新国'
# person.save()
#
# PeopleInfo.objects.filter(name= '周新国').update(name='郭靖')
#
#
# # 数据库操作:删除
# person = PeopleInfo.objects.get(name='郭靖')
# person.delete()
#
#
# BookInfo.objects.filter(name='周新国').delete()




# 基础查询
from book.models import BookInfo
BookInfo.objects.get(id=1)

BookInfo.objects.get(pk=2)

BookInfo.objects.count()

BookInfo.objects.all()

# 查询编号为1的图书
BookInfo.objects.filter(id=1)
# 查询书名包含'湖'的图书
BookInfo.objects.filter(name__contains='湖')
# 查询书名以'部'结尾的图书
BookInfo.objects.filter(name__endswith='部')
# 查询书名为空的图书
BookInfo.objects.filter(name__isnull=True)
# 查询编号为1或3或5的图书
BookInfo.objects.filter(id__in=[1,3,5])
# 查询编号大于3的图书
BookInfo.objects.filter(id__gt=3)
# 查询1980年发表的图书
BookInfo.objects.filter(pub_date__year='1980')
# 查询1990年1月1日后发表的图书
BookInfo.objects.filter(pub_date__gt='1990-1-1')




#查询阅读量大于等于评论量的图书
from django.db.models import F, Q

BookInfo.objects.filter(readcount__gte=F('commentcount'))

#查询阅读量大于2倍评论量的图书。
BookInfo.objects.filter(readcount__gt=F('commentcount')*2)


# 查询阅读量大于20，并且编号小于3的图书。

BookInfo.objects.filter(readcount__gt=20,id__lt=3)

BookInfo.objects.filter(readcount__gt=20).filter(id__lt=3)

# F和Q对象
# 查询阅读量大于20的图书，改写为Q对象如下。
BookInfo.objects.filter(Q(readcount__gt=20))

# 查询阅读量大于20，或编号小于3的图书，只能使用Q对象实现
BookInfo.objects.filter(Q(readcount__gt=20)|Q(id__lt=3))

# 查询编号不等于3的图书。
BookInfo.objects.filter(~Q(id=3))


#聚合函数
# 查询图书的总阅读量
from django.db.models import Sum
BookInfo.objects.aggregate(Sum('readcount'))


# 排序
BookInfo.objects.all().order_by('readcount')
BookInfo.objects.all().order_by('-readcount')

# 关联查询
# 查询书籍为1的所有人物信息

book = BookInfo.objects.get(id=1)
book.peopleinfo_set.all()


# 多对应的模型类对象.多对应的模型类中的关系类属性名
# 查询人物为1的书籍信息
from book.models import PeopleInfo
person = PeopleInfo.objects.get(id=3)
person.book


# 关联过滤查询
# 查询图书，要求图书人物为"郭靖"
book = BookInfo.objects.filter(peopleinfo__name='郭靖')
book

# 查询图书，要求图书中人物的描述包含"八"
book = BookInfo.objects.filter(peopleinfo__description__contains='八')
book


# 查询书名为“天龙八部”的所有人物
people = PeopleInfo.objects.filter(book__name='天龙八部')
people

# 查询图书阅读量大于30的所有人物
people = PeopleInfo.objects.filter(book__readcount__gt=30)
people


#查询数据
books = BookInfo.objects.all()
#导入分页类
from django.core.paginator import Paginator
#创建分页实例
paginator=Paginator(books,2)
#获取指定页码的数据
page_books = paginator.page(1)
#获取分页数据
total_page=paginator.num_pages