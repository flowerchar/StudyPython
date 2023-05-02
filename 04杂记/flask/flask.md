## 自动生成model(flask-sqlacodegen)

​	flask-sqlacodegen 'mysql://root:123456@127.0.0.1/mysql' --tables user --outfile "common/models/user.py" --flask



## 使用alchemy连接数据库，并获得对象

app.config['SQLALCHEMY_DATEBASE_URI']='mysql://root:123456@127.0.0.1/table'

db = SQLAlchemy(app)



## flask-script为命令行启动提供更多选择

```python
from flask-script import manager, Server ,Command
manager.add_command('runserver', Server(host='0.0.0.0',use_debugger=True,use_reload=True))


```



## flask-debugtoolbar为调试提供更多功能

```python
from flask_debugtoolbar import DebugToolbarExtensio
toolbar = DebugToolbarExtension(app)
```

