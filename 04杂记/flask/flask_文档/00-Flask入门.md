# Flask入门

### WEB工作原理

- C/S与B/S架构
- B/S架构工作原理
  - 客户端(浏览器) <=> WEB服务器(nginx) <=> WSGI(uWSGI) <=> Python(Flask) <=> 数据库(MySQL)
  - 说明：flask自带一个测试的WEB服务器，但是它仅仅适合于测试环境，不能用于生产环境。

### MVC与MTV框架

- MVC框架
  - M：Model，模型，即数据模型，负责数据的存取。
  - V：View，视图，负责数据的展示效果。
  - C：Controller，控制器，负责业务逻辑的处理。
- MTV框架
  - M：Model，模型，即数据模型，负责数据的存取。
  - T：Templates，模板，负责数据的展示效果。
  - V：View，视图函数，负责业务逻辑的处理。
- 总结：使用MVC或MTV就是为了解耦，可以提高开发维护的效率。

### Flask框架简介

- 说明：

  flask是一个轻量级的web框架，被称为微型框架。只提供了一个高效稳定的核心，其它全部通过扩展来实现。意思就是你可以根据项目需要进行量身定制，也意味着你需要不断学习相关的扩展库。

- 核心：

  - WSGI系统、调试、路由
  - 模板引擎(Jinja2，是flask核心开发者人员发开的)

- 安装：`pip install flask`

### 启动完整代码

-  完整代码

   ```python
   # 导入类库
   from flask import Flask

   # 创建应用实例
   app = Flask(__name__)

   # 添加视图函数
   @app.route('/')
   def index():
   	return 'Hello Flask!'   

   # 启动应用
   if __name__ == '__main__':
   	app.run()    
   ```


-  启动参数

   | 参数       | 说明                                       |
   | -------- | ---------------------------------------- |
   | debug    | 是否开启调试模式，默认为False；开启后会有出错调试信息，文件会自动加载。   |
   | threaded | 是否开启多线程，默认为Flase。                        |
   | host     | 指定主机，默认为'127.0.0.1'，设置为'0.0.0.0'后可以通过IP进制访问 |
   | port     | 指定端口，默认为5000。                            |

   > 启动示例：app.run(debug=True, threaded=True, host='0.0.0.0', port=5555)


### flask-script

- 说明：

  简单来说，该库就是flask终端启动的参数解析器；这样就可以不更改代码就能完成不同方式的启动。

- 安装：`pip install flask-script`

- 使用：

  ```python
    # 导入类库
    from flask_script import Manager

    # 创建对象
    manager = Manager(app)

    # 启动应用
    if __name__ == '__main__':
        manager.run()
  ```


- 启动参数：

  | 参数          | 说明      |
  | ----------- | ------- |
  | -?，--help   | 查看帮助    |
  | -h，--host   | 指定主机    |
  | -p，--port   | 主动端口    |
  | -d，--debug  | 开启调试模式  |
  | -r，--reload | 自动加载    |
  | --threaded  | 开启多线程   |
  | --processes | 指定多进程数量 |

  > 启动示例：python manage.py runserver -d -r -h 0.0.0.0 -p 5555

### flask使用

- 视图函数

  - 示例：

  ```python
  # 无参路由
  @app.route('/')
  def index():
      return '<h1>Hello Flask!</h1>'

  # 带参路由，可以传递多个参数
  @app.route('/welcome/<name>/<uid>/')
  def welcome(name, uid):
  	return 'Hello {} {}'.format(name, uid)

  # 指定参数类型，如：str(默认)、int、float、path
  @app.route('/user/<int:uid>/')
  def user(uid):
  	return 'Hello {}号'.format(uid)

  # path类型：类型仍然是str，只是将'/'当做普通字符处理而已
  @app.route('/path/<path:p>/')
  def path(p):
  	return p
  ```

  - 说明：

  ```
  1.路由末尾的'/'建议都加上，防止出现路由多敲'/'出现的问题
  2.若需要路由参数，参数需要放在<>中，对应的视图函数需要同名的参数
  3.路由参数可以指定多个，也可以指定类型
  4.常用参数类型：str(默认)、int、float、path，使用时放在参数前面，使用':'与参数连接
  5.path类型其实是str类型，只是将'/'作为普通字符处理罢了。
  ```

- 请求(request)

  ```python
  from flask import request

  # 请求，request中存放了所有的HTTP请求信息
  @app.route('/request/')
  def req():
      # 完整的路由地址
      # return request.url
      # 不包含GET参数的路由地址
      # return request.base_url
      # 只有协议主机和端口
      # return request.host_url
      # 只包含装饰器中的路由地址
      # return request.path
      # 请求方法的类型：GET、POST
      # return request.method
      # 客户端的IP
      # return request.remote_addr
      # args：GET参数；form：POST参数；values：GET和POST
      # return request.args.get('uid', '默认值')
      # headers：所有的请求头信息
      return request.headers.get('User-Agent')
  ```

- 响应(response)

  ```python
  from flask import make_response

  # 响应response
  @app.route('/response/')
  def response():
      # 直接返回字符串
      # return 'OK'
      # 可以在返回时指定状态码，默认都是200
      # return 'page not found', 404
      # 先用专门的函数构造一个响应对象，可以指定内容及状态码等
      resp = make_response('我是通过函数构造的响应', 404)
      # 设置响应头信息
      resp.headers['uid'] = 250
      return resp
  ```

- 重定向(redirect)

  ```python
  from flask import redirect, url_for

  # 重定向
  @app.route('/old/')
  def old():
      # return '原来的数据'
      # return redirect('/new/')
      # 根据视图函数名反向构造路由地址，参数是视图函数名
      # return url_for('new')
      return redirect(url_for('new'))

  @app.route('/new/')
  def new():
      return '新的数据'
  ```

- 反向构造路由(url_for)

  ```python
  # 反向构造路由
  @app.route('/urlfor/')
  def urlfor():
      # 不带参数的路由
      # return url_for('new')
      # 可以构造带参的路由，多出来的参数以GET形式传递
      # return url_for('user', uid=250, name='cuihua')
      # 构造完整(带协议主机和端口)路由，可以进行外部跳转
      return url_for('user', uid=250, name='cuihua', _external=True)
  ```

- 终止及错误定制

  ```python
  # 终止abort
  @app.route('/abort/')
  def err():
      # 终止代码执行，其实是向系统抛出指定异常
      # 系统捕获异常，按照统一的方案进行处理
      abort(404)
      return '正常'

  # 定制错误显示
  @app.errorhandler(404)
  def page_not_found(e):
  	return '是不是搞错了大哥？'
  ```


### 蓝本使用

- 说明：

  当大量的视图函数存放在一个文件中，很明显是不合适的。最好是根据功能模块进行划分，将相关的功能模块放在同一文件，蓝本就是用来解决这个问题的。

- 使用：

  - `user.py`

  ```python
  # 导入类库
  from flask import Blueprint, url_for

  # 创建对象，可以指定统一的前缀
  user = Blueprint('user', __name__, url_prefix='/user')

  # 添加视图函数
  @user.route('/login/')
  def login():
      # 当反向构造同一蓝本中的路由时，蓝本名可以省略，但是不能省略'.'
    	return url_for('.register')
    	return '欢迎登录'

  @user.route('/register/')
  def register():
  	return '欢迎注册'
  ```


  - `manage.py`

    ```python
    from user import user
    # 注册蓝本，注册时可以再次设置先关参数，而且优先级较高
    app.register_blueprint(user, url_prefix='/u')

    @app.route('/urlfor/')
    def urlfor():
        # 构造蓝本中的路由时参数这样传递：'蓝本名.视图函数名'
        return url_for('user.login')
    ```

