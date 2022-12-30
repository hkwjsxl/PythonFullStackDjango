## ORM优缺点

优点

> - 数据模型类都在一个地方定义，更容易更新和维护，也利于重用代码。
>
> - ORM 有现成的工具，很多功能都可以自动完成，比如数据消除、预处理、事务等等。
>
> - 它迫使你使用 MVC 架构，ORM 就是天然的 Model，最终使代码更清晰。
>
> - 基于 ORM 的业务代码比较简单，代码量少，语义性好，容易理解。
>
> - 新手对于复杂业务容易写出性能不佳的 SQL,有了ORM不必编写复杂的SQL语句, 只需要通过操作模型对象即可同步修改数据表中的数据.
>
> - 开发中应用ORM将来如果要切换数据库.只需要切换ORM底层对接数据库的驱动【修改配置文件的连接地址即可】

缺点

> - **ORM操作数据库的性能要比使用原生的SQL差。**
> - ORM 库不是轻量级工具，需要花很多精力学习和设置，甚至不同的框架，会存在不同操作的ORM。
> - 对于复杂的业务查询，ORM表达起来比原生的SQL要更加困难和复杂。
> - ORM 抽象掉了数据库层，开发者无法了解底层的数据库操作，也无法定制一些特殊的 SQL。【自己使用pymysql另外操作即可，用了ORM并不表示当前项目不能使用别的数据库操作工具了。】

## 模型表字段

~~~python
# 自动生成主键字段(ID)，后续较多使用pk自动查找主键
# choices参数
SEX_CHOICE = (
    (0, '保密'),
    (1, '男'),
    (2, '女'),
)
# choices=SEX_CHOICE
# 只要是choices参数的字段 如果你想要获取对应信息 固定写法 get_字段名_display()
# print(user_obj.get_gender_display()) # # 如果没有对应关系 那么展示的是值

# db_index=True创建数据库索引
# unique=True唯一索引
# verbose_name字段说明
# default默认值
# auto_now_add和auto_add首次创建都会入库当前时间
# auto_now_add 当数据添加时设置当前时间为默认值
# auto_now= 当数据添加/更新时, 设置当前时间为默认值
# db_column对应表中的字段
# 存大量文本
TextField
# 文件上传路径
FileField(upload_to='')

class Meta:
    # 指定表名，默认为app名小写_类名小写
    db_table = 'student'
    # 在admin站点中显示的名称
    verbose_name = '学生信息表'
    # 显示的复数名称
    verbose_name_plural = verbose_name
    # 抽象表，不在数据库建立出表
    abstract = True
~~~

## SQL命令中*的弊端

~~~python
SELECT `orm_stu`.`id`, `orm_stu`.`name`, `orm_stu`.`age`, `orm_stu`.`sex`, `orm_stu`.`create_time`, `orm_stu`.`class`, `orm_stu`.`description` FROM `orm_stu` LIMIT 21; args=()
"""
使用*会多一步查询字段的过程
使用字段而不使用*，省去了这一过程，可以提高效率
"""

~~~

## 基础查询API

~~~python
1.all()
2.first()
3.last()
4.filter()
5.count()
6.get()  # 返回与所给筛选条件相匹配的对象，返回结果有且只有一个，如果符合筛选条件的对象超过一个或者没有都会抛出错误。
7.order_by()  # 给‘-’是降序
8.exclude()  # 筛选条件不匹配的对象，返回queryset对象。
9.exists()  # 判断查询集中是否有数据
10.values(), values_list()  # 筛选字段，列表套字典，列表套元组
11.distinct()
12.reverse()
~~~

## 模糊查询

~~~python
字段名__方法，前加i表示不区分大小写，PS：iexact、icontains、istartswith、iendswith.
1.contains
2.startswith
3.endswith
4.gt,lt,gte,lte
5.range
6.in
7.isnull
1.日期查询：year、month、day、week_day、hour、minute、second
~~~

## 高阶查询

~~~python
from django.db.models import F, Q, Max, Min, Sum, Count, Avg
聚合查询,aggregate
分组查询,annotate,annotate前的values表示要分组的字段
# 查询每个班级学生的数学平均成绩
# Stu.objects.values('classmate').annotate(math_avg=Avg('math_score'))

"""
在操作字符类型的数据的时候，F不能够直接做到字符串的拼接
"""
# 将所有书的名称后面加上爆款两个字
from django.db.models.functions import Concat
from django.db.models import Value
models.Book.objects.update(title=Concat(F('title'), Value('爆款')))

# Q的高阶用法  能够将查询条件的左边也变成字符串的形式
q = Q()
q.connector = 'or'  # 修改条件
q.children.append(('maichu__gt',100))
q.children.append(('price__lt',600))
res = models.Book.objects.filter(q)
print(res)
~~~

## 正向查询和反向查询

~~~python
"""
关联字段在哪一方，哪一方就是正向，反之就是反向
正向查询：直接点关联字段
反向查询：related_name或表名小写_set（一对一直接表名小写）
"""
~~~

## Django中如何开启事务

~~~python
"""
事务
    ACID
        原子性
            不可分割的最小单位
        一致性
            跟原子性是相辅相成
        隔离性
            事务之间互相不干扰
        持久性
            事务一旦确认永久生效
事务的回滚 
    rollback
事务的确认
    commit
"""
from django.db import transaction
try:
    with transaction.atomic():
        # 在with代码快内书写的所有orm操作都是属于同一个事务
        # sql
        ...
except Exception as e:
    print(e)
print('执行其他操作')
~~~

## 数据库查询优化

~~~python
only与defer	
select_related与prefetch_related

"""
**queryset才有惰性查询**
orm语句的特点:
    惰性查询
        如果你仅仅只是书写了orm语句 在后面根本没有用到该语句所查询出来的参数
        那么orm会自动识别 直接不执行
"""
# only与defer
"""
only
	结果是一个列表套多个对象，这些对象默认只有only括号内的属性
	但是也可以点击括号内没有的属性，点击括号内没有的属性需要额外的走数据库操作
defer
	跟only刚好相反 
		对象里面唯独没有括号内指定的属性
"""

# select_related与prefetch_related
"""
select_related内部的本质是联表操作 inner join
	括号内只能放外键字段并且多对多不行
		括号内可以放多个外键字段
			select_related(外键字段1__外键字段2__外键字段3__...)
	将联表之后的结果全部查询出来封装到对象里面
	之后对象在点击表的字段的时候都无需再走数据库

prefetch_related内部本质是子查询
	内部通过子查询的方式将多张的表数据也封装到对象中
	这样用户在使用的时候也是感觉不出来的
	
select_related主要用于一对一，一对多。prefetch_related主要用于多对多，也可用于一对多
上述两种方式，在不同的场景下效率各有千秋
"""
~~~

## MTV与MVC模型

~~~python
# MTV:Django号称是MTV模型，其实是借鉴了MVC设计模式
Model：数据存储层，处理所有数据相关的业务，和数据库进行交互，并提供数据的增删改查；
Template：模板层（也叫表现层）具体来处理页面的显示；
View：业务逻辑层，处理具体的业务逻辑，它的作用是连通Model 层和 Template 。
# MVC:其实django本质也是MVC
Modle 代表数据存储层，是对数据表的定义和数据的增删改查；
View 代表视图层，是系统前端显示部分，它负责显示什么和如何进行显示；
Controller 代表控制层，负责根据从 View 层输入的指令来检索 Model 层的数据，并在该层编写代码产生结果并输出。

MTV 是 MVC 的一种细化，将原来 MVC 中的 V 层拿出来进行分离，视图的显示与如何显示交给 Template 层，而 View 层更专注于实现业务逻辑。
其实在 Django 是有 Controller 层的，只不过它由框架本身来实现，所以我们不用关心它。Django 更关注于M、T 和 V。

# vue框架:MVVM模型
~~~

## 多对多三种创建方式

~~~python
# 全自动:利用orm自动帮我们创建第三张关系表
	class Book(models.Model):
    name = models.CharField(max_length=32)
    authors = models.ManyToManyField(to='Author')
	class Author(models.Model):
    name = models.CharField(max_length=32)
	"""
	优点:代码不需要你写 非常的方便 还支持orm提供操作第三张关系表的方法...
	不足之处:第三张关系表的扩展性极差(没有办法额外添加字段...)
	"""
# 纯手动
	class Book(models.Model):
    name = models.CharField(max_length=32)
    
	class Author(models.Model):
    name = models.CharField(max_length=32)
  
  class Book2Author(models.Model):
    book_id = models.ForeignKey(to='Book')
    author_id = models.ForeignKey(to='Author')
  '''
  优点:第三张表完全取决于你自己进行额外的扩展
  不足之处:需要写的代码较多，不能够再使用orm提供的简单的方法
  不建议你用该方式
  '''

# 半自动（中介模型）
class Book(models.Model):
    name = models.CharField(max_length=32)
    authors = models.ManyToManyField(to='Author',
                                     through='Book2Author',
                                     through_fields=('book','author')
                                     )
class Author(models.Model):
    name = models.CharField(max_length=32)
    # books = models.ManyToManyField(to='Book',
    #                                  through='Book2Author',
    #                                  through_fields=('author','book')
    #                                  )
class Book2Author(models.Model):
    book = models.ForeignKey(to='Book')
    author = models.ForeignKey(to='Author')

"""
through_fields字段先后顺序
    判断的本质：
        通过第三张表查询对应的表 需要用到哪个字段就把哪个字段放前面
    你也可以简化判断
        当前表是谁 就把对应的关联字段放前面

半自动:可以使用orm的正反向查询，但是没法使用add,set,remove,clear这四个方法
"""

# 总结:你需要掌握的是全自动和半自动 为了扩展性更高 一般我们都会采用半自动(写代码要给自己留一条后路)
~~~

