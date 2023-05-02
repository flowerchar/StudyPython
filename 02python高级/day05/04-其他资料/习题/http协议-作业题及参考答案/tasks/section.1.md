# 每日必会题

1. **请简述浏览器访问HTTP服务器的过程。**

   1.   用户输入网址.
   2.   浏览器请求DNS服务器, 获取域名对应的IP地址.
   3.   请求连接该IP地址服务器.
   4.   发送资源请求. (HTTP协议)
   5.   web服务器接收到请求, 并解析请求, 判断用户意图.
   6.   获取用户想要的资源.
   7.   将资源返回给web服务器程序.
   8.   web服务器程序将资源数据通过网络发送给浏览器.
   9.   浏览器解析请求的数据并且完成网页数据的显示.

2. **简述TCP长/短连接的优点和缺点。**

   长连接可以省去较多的TCP建立和关闭的操作，节约时间。但是如果用户量太大容易造成服务器负载过高最终导致服务不可用

   短连接对于服务器来说实现起来较为简单，存在的连接都是有用的连接，不需要额外的控制手段。但是如果用户访问量很大, 往往可能在很短时间内需要创建大量的连接，造成服务器响应速度过慢

3. 实现代码，模拟实现服务器，获取通过浏览器客户端访问服务器的请求信息

   并将请求报文进行分行显示

   代码:

   ```python
   ''' 模拟服务器，获取客户端的请求报文 '''

   # 导入 socket 模块
   import socket

   # 封装一个 socket 服务器类
   class HTTPServer(object):
       def __init__(self):
           # 以 TCP 协议创建一个 socket
           self.__server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
           # 重用端口
           self.__server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
           # 绑定IP
           self.__server_socket.bind(('',8888))
           # 设置监听
           self.__server_socket.listen(128)

       # 服务器启动方法
       def run(self):
           # 接收客户端的请求
           client_socket, client_addr = self.__server_socket.accept()
           # 接收请求数据，并解码
           request_data = client_socket.recv(4096).decode()
           #按行进行分割
           requests = request_data.splitlines()
           # 遍历列表。输出请求报文内容
           for s in requests:
               print(s)
           #关闭socket
           client_socket.close()
           self.__server_socket.close()

   def main():
       # 创建服务器对象并启动
       http_server = HTTPServer()
       http_server.run()

   if __name__ == '__main__':
       main()

   ```

4. 实现代码，模拟实现客户端，组织请求报文，向服务器发送请求，获取服务器返回的响应报文数据 ，并将响应报文进行分行显示

   代码:

   ```python
   ''' 模拟客户端，向服务器发送请求，获取服务器响应 '''

   # 导入socket 模块
   import socket

   # 创建socket
   client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   #建立服务器连接
   client_socket.connect(('tlias3.boxuegu.com',80))

   # 拼接请求报文，模拟客户端发起请求
   # 请求行
   request_line = 'GET / HTTP/1.1\r\n'
   # 请求头
   request_head = 'Host: www.baidu.com\r\n'

   request_head += 'Connection: close\r\n'
   # 拼接请求报文
   request_data = request_line + request_head + '\r\n'

   # 发送请求
   client_socket.send(request_data.encode())

   # 接收服务器的响应数据
   response_data = b''
   # 服务器在回传数据 时，可能不是一次性将数据发送回来，所以要一直接收
   while True:
       # 循环接收数据，因为服务器的数据可以不是一次性发过来的
       recv_data = client_socket.recv(1024)
       # 如果有数据就进行拼接
       if recv_data:
           response_data += recv_data
       else:
           break

   # 解码
   response_data = response_data.decode()

   # 分割
   responses = response_data.split('\r\n\r\n',1)

   # 遍历显示
   for s in responses:
       print(s)

   # 关闭连接
   client_socket.close()

   ```

   ​

