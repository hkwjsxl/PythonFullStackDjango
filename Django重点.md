# Django

### 简述python三大主流web框架

~~~python
"""
django
	大而全，类似于航空母舰
	但是有时候过于笨重
flask
	小而精，类似于游骑兵(单行代码就可以起一个flask服务)
	第三方组件很多，但是有时候也会受限于第三方
tornado
	异步非阻塞
	速度非常快

SANIC
FASTAPI
...
"""
~~~

### WSGI，ASGI跟wsgiref和uwsgi是什么关系

~~~python
WSGI、ASGI是协议，ASGI基于WSGI
wsgiref和uwsgi是实现该协议的功能模块
~~~

### 简述无名有名分组

~~~python
将匹配到的内容按位置参数传递到视图函数中
将匹配到的内容按关键字参数传到到试图函数中
~~~

### 简述反向解析以及名称空间

~~~python
反向解析(本质)就是指通过一些方法，得到一个结果，该结果可以访问到对应的url并触发视图函数的运行
名称空间就是解决多个app下出现相同的别名，反向解析不会自动识别应用的前缀

反向解析的应用场景，是因为在软件开发初期，url地址的路径设计可能并不完美，后期需要进行调整，如果项目中很多地方使用了该路径，一旦该路径发生变化，就意味着所有使用该路径的地方都需要进行修改，这是一个非常繁琐的操作。
别名不能出现冲突!!!
# 别名如果发生冲突，未声明命名空间时，不同app下如果有相同的路由别名，反向解析会解析到最下面的app，会发生覆盖
~~~

### MTV与MVC模型

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

### FBV和CBV的区别

~~~python
FBV与CBV在路由匹配上本质是一样的，都是路由对应函数的内存地址
CBV特点：能够直接根据请求方式的不同自动匹配到对应的方法执行
~~~

### 简述CBV流程

~~~python
特点：能够根据请求方式的不同自动匹配触发对应的方法执行
CBV本质上也是FBV
自定义类调用并执行View中的as_view方法，View类中维护了一个列表，列表中存有8中请求方式，
as_view函数返回一个view函数，view函数返回一个dispatch函数，
dispatch函数中将传入的请求方式变小写，通过反射去列表中查找是否有对应的请求方式，
有的话往后执行，没有就返回信息-不允许该请求方式
~~~

### 数据库查询优化

~~~python
# only与defer	
# select_related与prefetch_related

"""
**queryset才有惰性查询**
orm语句的特点:
    惰性查询
        如果你仅仅只是书写了orm语句 在后面根本没有用到该语句所查询出来的结果
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

### Restful规范

~~~python
https://www.cnblogs.com/hkwJsxl/p/16581564.html
~~~

### Web服务器和Web应用程序的区别

~~~python
Web应用程序主要是完成web应用的业务逻辑的处理，Web服务器则主要是应对外部请求的接收、响应和转发。
需要使用web服务器启动运行，web应用程序才能被用户访问到。
而django框架中，我们之所以只有一个web应用程序就跑起来了，是因为我们在终端执行了一个命令，
python manage.py runserver。这个命令启动了django框架中内置提供的测试web服务器。
~~~

### 请描述一个客户端请求从发起到返回的过程（用django来描述）；

~~~python
用户从浏览器发起一个请求，请求来了之后到wsgi解析封装数据，
然后<请求拦截中间件>（process_request），
接着通过url路由匹配，分发到视图，
有render的走中间件的process_view，
需要连接数据库的连接数据库，不需要连接数据库的<响应拦截中间件>（process_response），
最后wsgi打包数据直接响应给浏览器。
~~~

![微信图片_20221221201256](https://img2023.cnblogs.com/blog/2570053/202212/2570053-20221221202307977-1652893441.png)

### 请问*Django project*和*Django app*之间有什么区别和联系？

~~~python
一个django项目可以有多个app，每个app处理不同的业务逻辑
~~~

### 请详细说明Django中间件处理请求的流程(各个处理函数的执行顺序)

~~~python
django中间件中一共有五个方法：
	process_request
	process_response
	process_view
	process_exception
	process_template_response
主要常用为前两个，当用户发起请求时，会从上到下依次经过每一个中间件，这个时候会触发process_request函数，如果函数返回None，则继续到view视图中，返回HttpResponse响应对象则直接从当前中间件的process_reponse函数返回，正常情况下，视图层处理完后，返回执行中间件process_response函数，最后返回给浏览器
process_view在process_request和process_response之间执行
process_exception在出错时执行
process_template_response在视图层中返回的对象有render方法时执行
~~~

### 请问django中如何进行路由分发操作？

~~~python
在应用下创建一个urls.py，将关于该应用的逻辑处理放到url里面，然后在总路由下导入该应用的urls
~~~

### get和filter操作出的结果集是什么数据类型, 有什么区别？

~~~python
get取到的是模型类对象
filter取到的queryset集合

queryset集合可以包含多个模型类对象
~~~

### create和save方法有什么区别？

~~~python
save方法要分为两步，save才是最后操作数据库的语句
create直接操作数据库，一步到位
~~~

### 重定向

~~~python
一、301和302的异同。
1.相同之处：
   301和302状态码都表示重定向，具体点说就是浏览器在拿到服务器返回的这个状态码后会自动跳转到一个新的URL地址（浏览器会从响应头Location中获取新地址），用户看到的效果都是输入地址A后瞬间跳转到了另一个地址B
2.不同之处：
　　301表示旧地址A的资源已经被永久地移除了，即这个资源不可访问了。搜索引擎在抓取新内容的同时也将旧的网址转换为重定向之后的地址；
　　302表示旧地址A的资源还在，即这个资源仍然可以访问，这个重定向只是临时地从旧地址A跳转到地址B，搜索引擎会抓取新的内容、并且会保存旧的网址。 从SEO层面考虑，302要好于301

二、重定向原因：
1.网站调整（如改变网页目录结构）；
2.网页被移到一个新地址；
3.网页扩展名改变(如应用需要把.php改成.Html或.shtml)。
这种情况下，如果不做重定向，则用户收藏夹或搜索引擎数据库中旧地址只能让访问客户得到一个404页面错误信息，访问流量白白丧失；再者某些注册了多个域名的网站，也需要通过重定向让访问这些域名的用户自动跳转到主站点等。
~~~

