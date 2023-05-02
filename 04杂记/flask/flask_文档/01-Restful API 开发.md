# Restful API 开发

### Restful简介

- Restful API 开发其实就针对资源及对资源的各种操作展开。

- Restful 就是将对网络资源的操作抽象为HTTP协议的不同方法。

  | 方法     | 行为     | 示例                                |
  | ------ | ------ | --------------------------------- |
  | GET    | 获取资源信息 | http://127.0.0.1:5000/source/     |
  | GET    | 获取指定资源 | http://127.0.0.1:5000/source/250/ |
  | POST   | 创建新的资源 | http://127.0.0.1:5000/source/     |
  | PUT    | 修改指定资源 | http://127.0.0.1:5000/source/250/ |
  | DELETE | 删除指定资源 | http://127.0.0.1:5000/source/250/ |

- 数据：通常都采用JSON进行传输。

- 测试工具：postman是一款非常好用的测试工具，能够轻松模拟各种请求。

### flask-restful

- 说明：是一个快速进行restful api 开发的扩展库，使用非常方便。

- 安装：`pip install flask-restful`

- 使用：

  ```python
  from flask_restful import Api, Resource

  # 资源类
  class UserAPI(Resource):
      def get(self, uid):
          return {'UserAPI:GET': '获取'+str(uid)+'用户信息'}

      def put(self, uid):
          return {'UserAPI:PUT': '修改'+str(uid)+'用户信息'}

      def delete(self, uid):
          return {'UserAPI:DELETE': '删除'+str(uid)+'用户信息'}
      
  class UserListAPI(Resource):
  	def get(self):
        	return {'UserListAPI:GET': '获取用户列表'}

    	def post(self):
        	return {'UserListAPI:POST': '注册新用户'}   
      
  # 创建对象
  api = Api(app)

  # 添加资源类，可以指定多个路径
  api.add_resource(UserAPI, '/users/int:uid/')
  api.add_resource(UserListAPI, '/users/', '/u/')
  # 若初始化是分开进行的，记得一定要添加资源之后
  # api.init_app(app)
  ```


###flask-httpauth

- 说明：专门用来进行身份认证的扩展库，使用非常方便。

- 安装：`pip install flask-httpauth`

- 使用：    

  ```python
  # 导入认证类库
  from flask_httpauth import HTTPBasicAuth

  # 创建认证对象
  auth = HTTPBasicAuth()

  # 认证回调函数，True表示认证成功，False表示认证失败
  @auth.verify_password
  def verify_password(username, password):
      if username == 'Jerry' and password == '123456':
          return True
      return False

  # 认证错误定制
  @auth.error_handler
  def unauthorized():
      return jsonify({'error': 'Unauthorized Access'}), 403

  class UserAPI(Resource):
      # 保护指定路由
      @auth.login_required
      def get(self, uid):
          return {'UserAPI:GET': '获取'+str(uid)+'用户信息'}
        
  class UserListAPI(Resource):
      # 统计认证
      decorators = [auth.login_required]  
  ```


### 基于token的认证

- 说明：cookie的机制太麻烦，每次携带用户名和密码又不安全。


- 使用：

  ```python
    @auth.verify_password
    def verify_password(username_or_token, password):
        if username_or_token == 'Jerry' and password == '123456':
            g.username = username_or_token
            return True
        # 再次认证
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(username_or_token.encode('utf8'))
        except:
            return False

        g.username = data['username']
        return True
      
    # 获取用户身份信息(token)
    @app.route('/get_token/')
    @auth.login_required
    def generate_token():
        s = Serializer(app.config['SECRET_KEY'], expires_in=app.config['TOKEN_LIFETIME'])
        token = s.dumps({'username': g.username})
        return jsonify({'token': token.decode('utf8'), 'expires': app.config['TOKEN_LIFETIME']})  
  ```

  ​