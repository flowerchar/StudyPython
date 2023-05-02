# 每日必会题

1. **请简述什么是TCP，以及TCP的特点。**

   TCP:英文全拼(Transmission Control Protocol)简称传输控制协议，它是一种面向连接的、可靠的、基于字节流的传输层通信协议.

   TCP通信需要经过创建连接、数据传送、终止连接三个步骤。

   
3. **简述TCP在建立连接时的三次握手的过程。**


      TCP在建立连接时需要通过三次握手过程来完成。

   - 第一次握手：Client将标志位SYN置为1，随机产生一个值seq=J，并将该数据包发送给Server，Client进入SYN_SENT状态，等待Server确认。
   - 第二次握手：Server收到数据包后由标志位SYN=1知道Client请求建立连接，Server将标志位SYN和ACK都置为1，ack (number )=J+1，随机产生一个值seq=K，并将该数据包发送给Client以确认连接请求，Server进入SYN_RCVD状态。
   - 第三次握手：Client收到确认后，检查ack是否为J+1，ACK是否为1，如果正确则将标志位ACK置为1，ack=K+1，并将该数据包发送给Server，Server检查ack是否为K+1，ACK是否为1，如果正确则连接建立成功，Client和Server进入ESTABLISHED状态，完成三次握手，随后Client与Server之间可以开始传输数据了。

   ​

4. **简述TCP在断开连接时四次挥手的过程。**

   TCP在断开连接时，需要通过四次挥手的过程来完成。

   - 第一次挥手：Client发送一个FIN，用来关闭Client到Server的数据传送。
   - 第二次挥手：Server收到FIN后，发送一个ACK给Client，确认序号为收到序号+1。
   - 第三次挥手：Server发送一个FIN，用来关闭Server到Client的数据传送。
   - 第四次挥手：Client收到FIN后，接着发送一个ACK给Server，确认序号为收到序号+1。

   ​

5. **实现局域网内的点对点聊天机器人程序。**

   **使用TCP协议编写 socket 程序，分别实现消息的发送端和接收端**

   **服务端记录客户端发送的消息，并进行随机回复**

   **当客户端发送Bye时结束聊天**

   TCPServer.py：

   ```python
   ''' 使用TCP协议实现一个尬聊机器人 （服务端）'''

   # 导入模块
   import socket
   import random

   # 封装一个类
   class ChatServer(object):
       def __init__(self):
           # 创建一个用来保存聊天内容的列表
           self.__list = ['hi','Hello','你好']
           # 以TCP协议初始化 socket
           self.__server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
           # 利用端口
           self.__server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
           # 绑定IP和端口
           self.__server_socket.bind(('',7777))
           # 设置监听数量
           self.__server_socket.listen(128)

       # 启动服务的方法
       def run(self):
           # 接收客户端聊天请求，目前只能单任务聊天
           client_socket, client_addr = self.__server_socket.accept()
           # 循环接收聊天信息
           while True:
               # 接收客户端发来的数据
               recv_data = client_socket.recv(1024).decode()
               # 显示接收数据的信息并输出
               print(client_addr[0], ' 说: ',recv_data)
               # 将客户端发来的信息保存到列表中，模拟自动学习
               self.__list.append(recv_data)
               # 判断如果客户端发送 bye ,则回复bye，结束循环，停止聊天
               if recv_data == 'Bye':
                   client_socket.send('Bye'.encode())
                   break
               else:
                   # 如果不是bye，那么从信息列表中随机取得一个下标
                   rand_idx = random.randint(0,len(self.__list) - 1)
                   # 通过随机下标获取一条信息
                   send_data = self.__list[rand_idx]
                   # 将信息发送给客户端
                   client_socket.send(send_data.encode())

   def main():
       # 启动服务器
       chat_server = ChatServer()
       chat_server.run()

   if __name__ == '__main__':
       main()

   ```

   TCPClient.py：

   ```python
   ''' 使用TCP协议实现一个尬聊机器人  客户端'''

   # 导入模块
   import socket

   # 封装一个聊天对象类
   class Person(object):
       def __init__(self):
           # 以 TCP 形式初始化 socket 对象
           self.__client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
           self.__client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
           self.__client_socket.connect(('', 7777))

       # 开始聊天
       def start_chat(self):
           # 死循环保证持续聊天
           while True:
               # 输入一条消息
               send_data = input('我:')
               # 客户端将消息发给机器人
               self.__client_socket.send(send_data.encode())
               # 接收机器人回复的消息并解码输出
               recv_data = self.__client_socket.recv(1024).decode()
               print('机器人: %s' %recv_data)
               # 如果接收到的是 Bye，那么结束聊天
               if recv_data == 'Bye':
                   self.__client_socket.close()
                   print('over')
                   break

   def main():
       tom = Person()
       tom.start_chat()

   if __name__ == '__main__':
       main()

   ```

   **知识点回顾**

   - 列表
     - 列表是可变对象，可以对列表中的内容进行添加和删除。
     - 列表通过索引可获取相应位置上的数据
   - 随机数
     - 使用 random 模块来得到随机数
     - random.randint(a, b) 得到一个 a, b 之间的随机数
     - 函数返回数字N ，N 为a 到b 之间的数字（a <= N <= b），包含a 和b。

