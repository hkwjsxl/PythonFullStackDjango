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
SEX_CHOICE = (
    (0, '保密'),
    (1, '男'),
    (2, '女'),
)
# choices=SEX_CHOICE
# db_index=True创建数据库索引
# unique=True唯一索引
# verbose_name字段说明
# default默认值
# auto_now_add和auto_add首次创建都会入库当前时间
# auto_now_add 当数据添加时设置当前时间为默认值
# auto_now= 当数据添加/更新时, 设置当前时间为默认值
# db_column对应表中的字段

class Meta:
    # 指定表名，默认为app名小写_类名小写
    db_table = 'student'
    # 在admin站点中显示的名称
    verbose_name = '学生信息表'
    # 显示的复数名称
    verbose_name_plural = verbose_name
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
~~~
