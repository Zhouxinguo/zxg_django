from django.db import models

# Create your models here.

"""
1.定义属性字段不能用连续的下划线
2.类型 -- mysql的类型
3.选项
    CharField 必须设置max_length
4. 改变表的名称
    默认子应用名类名 
    修改表的名字  
"""


class BookInfo(models.Model):
    name = models.CharField(max_length=20, unique=True)
    pub_data = models.DateField(null=True)
    readcount = models.IntegerField(default=0)
    commentcount = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'bookinfo'  # 修改名字
        verbose_name = '书记管理'  # admin 站点管理 了解

    def __str__(self):
        return self.name


class PeopleInfo(models.Model):
    # 定义有序列表
    GENDER_CHOICE = (
        (1, 'male'),
        (2, 'female')
    )
    name = models.CharField(max_length=20, unique=True)
    gender = models.SmallIntegerField(choices=GENDER_CHOICE, default=1)
    description = models.CharField(max_length=100, null=True)
    is_delete = models.BooleanField(default=False)

    # 系统会自动为外键添加_id
    # 外键的级联操作  详见课件
    # 1对多  书籍  对  人物
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    class Meta:
        db_table = 'peopleinfo'

    def __str__(self):
        return self.name

class Dog(object):
    pass

class Person(object):
    pass