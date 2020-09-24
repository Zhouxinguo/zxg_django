from django.shortcuts import render

# Create your views here.

from book.models import BookInfo
def index(request):
    books = BookInfo.object

# 方式一

book = BookInfo(
    name= 'Django',
    pub_date = '2000-1-1',
    readcount = 10
)
book.save()


# 方式二

BookInfo.object.create(
    name = '测试开发入门',
    pub_date = '2020-1-1',
    readcount=100
)


############修改数据##########

# 方式1
# select * from bookinfo where id=6
book = BookInfo.object.get(id=6)

book.name = '运维开发入门'
book.save()


# 方式2
# filter 过滤
BookInfo.object.filter(id=6).update(name='爬虫入门',commentcount=666)


#########删除数据#########


# 方式2
BookInfo.objects.get(id=6).delete()
BookInfo.objects.filter(id=5).delete()


############ 查询 #########

# get查询单个结果,查询不到会报错
try:
    book = BookInfo.objects.get(id=1)
except BookInfo.DoesNotExist:
    print('查询结果不存在')

# all查询多个结果
BookInfo.objects.all()
from book.models import PeopleInfo
PeopleInfo.objects.all()

# count查询结果数量
BookInfo.objects.all().count()
BookInfo.objects.count()


########### 过滤查询 ##############
# 实现SQl 中的where功能 包括

# filter过滤多个结果
# exclude 排除掉符合条件剩下的结果
# get 过滤单一的结果

# 规则类名.objects.filter(属性名__运算符=值)  获取n个结果 n=0,1,2.....
# 规则类名.objects.exclude(属性名__运算符=值)  获取n个结果 n=0,1,2.....
# 规则类名.objects.get(属性名__运算符=值)  获取1个结果 或者 异常

# 查询编号为1的图表
book = BookInfo.objects.get(id=1)
book = BookInfo.objects.get(id__exact=1)

BookInfo.objects.get(pk=1)
BookInfo.objects.get(id=1)
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
BookInfo.objects.filter(pub_data__year=1980)

# 查询1990年1月1日后发表的图书
BookInfo.objects.filter(pub_data__gt='1990-1-1')



#######################################

from django.db.models import F

# 使用:2个属性的比较

# 查询阅读量大于等于评论量的图书
BookInfo.objects.filter(readcount__gte=F('commentcount'))


################################

# 并且查询
# 查询阅读量大于20,并且编号小于3的图书
BookInfo.objects.filter(readcount__gt=20).filter(id__lt=3)

BookInfo.objects.filter(readcount__gt=20,id__lt=3)


# 或者查询
# 查询阅读量大于20,或者编号小于3的图书

from django.db.models import Q

BookInfo.objects.filter(Q(readcount__gt=20)|Q(id__lt=3))