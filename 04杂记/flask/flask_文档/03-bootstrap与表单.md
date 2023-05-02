# bootstrap与表单

### flask-boostrap

- 说明：在flask中使用bootstrap，可以通过该扩展库完成。

- 安装：`pip install flask-bootstrap`

- 使用：

  ```python
  from flask_bootstrap import Bootstrap

  bootstrap = Bootstrap(app)
  ```

- 模板

  ```html
  {# 继承自bootstrap基础模板 #}
  {% extends 'bootstrap/base.html' %}

  {% block title %}标题{% endblock %}

  {% block content %}
      <div class="container">默认内容</div>
  {% endblock %}
  ```

- bootstrap基础模板中的block

  | block   | 说明          |
  | ------- | ----------- |
  | doc     | 整个HTML文档    |
  | html    | 整个html标签    |
  | head    | 整个head标签    |
  | metas   | 一组meta标签    |
  | styles  | 一组link标签    |
  | body    | 整个body标签    |
  | navbar  | 导航条         |
  | content | 页面内容        |
  | scripts | 一组scripts标签 |

  > 提示：当重写一个block后，原来的显示效果全没了，很可能是因为没有写`{{ super() }}`

### 项目基础模板定制

- 见视频《03-项目基础模板定制》

### 加载静态资源

- flask中静态资源默认存放在static目录下，因此目录结构如下：

  ```
  project/		# 项目目录
  	manage.py			# 启动控制文件
  	templates/			# 模板文件目录
  	static/				# 静态资源目录
  		img/				# 图片
  		css/				# css文件
  		js/					# js文件
  		favicon.ico			# 收藏夹图标
  ```

- 加载静态资源文件

  ```html
  {# 继承自自定义的基础模板 #}
  {% extends 'base.html' %}

  {% block title %}用户登录{% endblock %}

  {% block page_content %}
      <h1>欢迎登录...</h1>
      <div class="test"></div>
      {# 加载图片资源 #}
      <img width="300" src="{{ url_for('static', filename='img/liuyan.jpg') }}">
  {% endblock %}

  {% block styles %}
      {{ super() }}
      {# 加载CSS文件 #}
      <link href="{{ url_for('static', filename='css/common.css') }}" type="text/css" rel="stylesheet" />
  {% endblock %}

  {% block head %}
      {{ super() }}
      {# 加载网站收藏夹小图标 #}
      <link rel="icon" type="image/x-icon" href="{{ url_for('static', filename='favicon.ico') }}" />
  {% endblock %}

  {% block scripts %}
      {{ super() }}
      {# 加载JS文件 #}
      <script type="text/javascript" src="{{ url_for('static', filename='js/common.js') }}"></script>
  {% endblock %}
  ```

### 原生表单

- 准备模板文件

  ```html
  <form method="get" action="{{ url_for('check') }}">
      用户名：<input name="username" /><br />
      <input type="submit" />
  </form>
  ```

- 添加视图函数，渲染模板文件

  ```python
  @app.route('/login/')
  def login():
      return render_template('login.html')
  ```

- 校验提交的请求

  ```python
  @app.route('/check/', methods=['GET', 'POST'])
  def check():
      # args：所有的GET参数
      # return request.args.get('username', '提交失败')
      # form：所有的POST参数
      # return request.form.get('username', '提交失败')
      # values：所有的GET/POST参数
      return request.values.get('username', '提交失败')
  ```

- 一个路由可以接收多种请求

  ```python
  @app.route('/login/', methods=['GET', 'POST'])
  def login():
      if request.method == 'POST':
          return request.form.get('username', '登录失败')
      return render_template('login.html')
  ```

### flask-wtf

- 说明：表单处理的扩展库，提供了CSRF、字段校验等实用功能，实用非常方便。

- 安装：`pip install flask-wtf`

- 使用：

  - 创建表单类：

  ```python
  # 导入表单类的基类
  from flask_wtf import FlaskForm
  # 导入字段类型
  from wtforms import StringField, SubmitField
  # 导入相关验证器
  from wtforms.validators import Length

  # 创建表单类
  class NameForm(FlaskForm):
      # name = StringField('用户名')
      # submit = SubmitField('提交')
      name = StringField('用户名', validators=[Length(3, 6, message='用户名必须是3~6个字符')])
      submit = SubmitField('提交')
  ```

  - 添加视图函数，创建表单对象，并分配的模板中

  ```python
    @app.route('/', methods=['GET', 'POST'])
    def index():
        # 创建表单对象
        form = NameForm()
        # 判断是否是有效的提交
        if form.validate_on_submit():
            return form.name.data
        # 在模板文件中渲染表单
        return render_template('form.html', form=form)  
  ```


- 原生渲染表单

  ```html
  {# 原生渲染 #}
  <form method="post">
      {# CSRF字段 #}
      {{ form.hidden_tag() }}
      {# name字段 #}
      {{ form.name.label() }}{{ form.name(id='xx', class='yy') }}
      {% for e in form.name.errors %}
          <div>{{ e }}</div>
      {% endfor %}
      {# 提交按钮 #}
      {{ form.submit() }}
  </form>
  ```

- 使用bootstrap进行渲染

  ```html
  {% extends 'bootstrap/base.html' %}

  {# 导入快速渲染表单的宏 #}
  {% from 'bootstrap/wtf.html' import quick_form %}

  {% block title %}bootstrap渲染表单类{% endblock %}

  {% block content %}
      <div class="container">
          {# 在合适的位置渲染表单 #}
          {{ quick_form(form) }}
      </div>
  {% endblock %}
  ```

- POST重定向到GET：浏览器会记录最后的请求状态，若最后请求时POST，点击刷新时会提示再次提交表单。

  ```python
  @app.route('/', methods=['GET', 'POST'])
  def index():
      # 创建表单对象
      form = NameForm()
      # 判断是否是有效的提交
      if form.validate_on_submit():
          session['name'] = form.name.data
          return redirect(url_for('index'))
      name = session.get('name')
      # 在模板文件中渲染表单
      return render_template('form2.html', form=form, name=name)
  ```

- 常见字段类型

  | 字段类型          | 说明                  |
  | ------------- | ------------------- |
  | StringField   | 普通文本                |
  | SubmitField   | 提交按钮                |
  | PasswordField | 密文文本                |
  | HiddenField   | 隐藏字段                |
  | RadioField    | 单选框                 |
  | BooleanField  | 复选框                 |
  | SelectField   | 下拉框                 |
  | FileField     | 文件上传                |
  | TextAreaField | 文本域                 |
  | IntegerField  | 文本字段，值为整数           |
  | FloatField    | 文本字段，值为浮点数          |
  | DateField     | datetime.date类型     |
  | DateTimeField | datetime.datetime类型 |

- 常见验证器

  | 验证器          | 说明                  |
  | ------------ | ------------------- |
  | Length       | 规定字符长度              |
  | DataRequired | 确保字段有值(提示信息与所写的不一致) |
  | Email        | 邮箱格式                |
  | IPAddress    | IP地址                |
  | NumberRange  | 数值的范围               |
  | URL          | 统一资源定位符格式           |
  | EqualTo      | 验证两个字段的一致性          |
  | Regexp       | 正则校验                |

- 自定义字段验证函数

  ```python
  # 创建表单类
  class NameForm(FlaskForm):
    	。。。
  	# 字段校验函数：'validate_字段名'
      def validate_name(self, field):
          if len(field.data) < 6:
              raise ValidationError('用户名不能少于6个字符')
  ```

### 消息闪烁

- 说明：

  当用户发出请求后，状态发生了改变，需要系统给出警告提示等信息时，通常都是弹出一条消息，指示用户下一步的操作，用户可以手动关闭或自动消失，整个过程不会影响页面的正常显示。

- 使用：

  - 在需要闪烁消息时，使用`flash`函数保存闪烁消息

  ```python
  @app.route('/', methods=['GET', 'POST'])
  def index():
      # 创建表单对象
      form = NameForm()
      # 判断是否是有效的提交
      if form.validate_on_submit():
          last_name = session.get('name')
          if last_name and last_name != form.name.data:
              flash('大哥，又换签名了^_^')
          session['name'] = form.name.data
          return redirect(url_for('index'))
      name = session.get('name')
      # 在模板文件中渲染表单
      return render_template('form2.html', form=form, name=name)
  ```

  - 在模板文件中提供`get_flashed_messages`函数获取闪烁消息并渲染：

  ```html
  {% for message in get_flashed_messages() %}
  <div class="alert alert-warning alert-dismissible" role="alert">
  	<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span>
  	</button>
  	{{ message }}
  </div>
  {% endfor %}
  ```

  > 说明：上面是从bootstrap粘贴的可消失的警告框。

### flask-moment

- 说明：专门负责数据本地化显示的扩展库，使用非常方便。

- 安装：`pip install flask-moment`

- 使用：

  - python代码：

  ```python
  from flask_moment import Moment

  moment = Moment(app)

  @app.route('/moment/')
  def mom():
      from datetime import datetime, timedelta
      current_time = datetime.utcnow() + timedelta(seconds=-360)
      return render_template('mom.html', current_time=current_time)
  ```

  - 模板文件：

  ```html
  {# 加载jQuery #}
  {{ moment.include_jquery() }}

  {# 加载moment #}
  {{ moment.include_moment() }}

  {# 设置语言 #}
  {{ moment.locale('zh-CN') }}

  {# 简单的格式化时间显示 #}
  <div>时间：{{ moment(current_time).format('LLLL') }}</div>
  <div>时间：{{ moment(current_time).format('LLL') }}</div>
  <div>时间：{{ moment(current_time).format('LL') }}</div>
  <div>时间：{{ moment(current_time).format('L') }}</div>

  {# 自定义格式化时间显示 #}
  <div>自定义：{{ moment(current_time).format('YYYY-MM-DD HH:mm:ss') }}</div>

  {# 显示时间差 #}
  <div>发表于：{{ moment(current_time).fromNow() }}</div>
  ```

### 练习：

- 完成用户的注册登录功能