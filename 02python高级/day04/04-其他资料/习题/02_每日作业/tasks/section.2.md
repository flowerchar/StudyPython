# 每日练习题

1. TCP是什么?

   **TCP协议，传输控制协议（英语：Transmission Control Protocol，缩写为 TCP）**是一种面向连接的、可靠的、基于字节流的传输层通信协议，由IETF的RFC 793定义

   ​

2. TCP通信流程?

   TCP通信需要经过**创建连接、数据传送、终止连接**三个步骤。

   ​

3. **TCP有什么特点?**

   - 面向连接

     通信双方必须先建立连接才能进行数据的传输，双方都必须为该连接分配必要的系统内核资源，以管理连接的状态和连接上的传输。

     双方间的数据传输都可以通过这一个连接进行。

     完成数据交换后，双方必须断开此连接，以释放系统资源。

      **这种连接是一对一的，因此TCP不适用于广播的应用程序，基于广播的应用程序请使用UDP协议**

   - 可靠传输

     - **TCP采用发送应答机制**
     - **超时重传**
     - **错误校验**
     - **流量控制和阻塞管理**

   ​

5. 怎么区分服务器端和客户端?

   服务器端:提供服务的一方

   而客户端:需要被服务的一方

   ​

6. TCP服务器是否需要绑定?为什么?

   需要绑定,不然客户端无法连接到服务器

   ​

7. TCP客户端是否需要绑定?为什么?

   不需要绑定,因为客户端是去主动连接服务器的

   ​

8. TCP服务器中listen方法的作用?

   使套接字变为可以被动连接

   ​

9. TCP客户端中connect方法的作用?

   连接到目标服务器

   ​

10. 当一个TCP客户端连接服务器时，服务端会有一个新的套接字，这个套接字是什么?有什么作用?

   这个套接字是管理当前客户端和服务器连接的套接字,并非客户端的套接字

   使用这个套接字来和客户端之间收发消息

   ​

11. 服务器如何判断客户端是否已经断开连接?

    可以通过返回的数据长度来判断,如果返回数据长度为0,则客户端已经断开连接
    ​

13. TCP客户端的创建流程?

    - 创建客户端套接字
    - 使用connect方法连接服务器地址
    - 收发消息

    ​

14. **TCP服务器的创建流程?**

    - 创建TCP套接字
    - bind绑定ip和端口
    - 使用listen方式使套接字变为可以被动连接
    - accept等待客户端连接
    - 收发消息 ​

16. 理解并画出**tcp**运行流程

    见xmind总结

    ​

17. **完成tcp客户端代码的练习**

    见课件

    ​

18. **完成tcp服务器代码的练习**

    见课件

    ​

19. 写一个简易版聊天机器人，包含如下功能：

    ```
    1.自己写tcp客户端以及服务端
    2.发送"你好"、"hello"等，会回复"你好"
    3.发送"名字"、"name"等关键词，会回复"我是python29号"
    4.发送"时间"、"time"等关键词，会回复"当前时间是：xx:xx:xx(当前时间)"
    	提示：显示时间：time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    ……自行添加
    ```

    参考代码:

    客户端:

    ```python
    from socket import *

    # 创建socket
    tcp_client_socket = socket(AF_INET, SOCK_STREAM)

    # 目的信息
    server_ip = input("请输入服务器ip:")
    server_port = int(input("请输入服务器port:"))

    # 链接服务器
    tcp_client_socket.connect((server_ip, server_port))
    while True:
        # 提示用户输入数据
        send_data = input("请输入要发送的数据：")
        if send_data == "quit" or send_data == "exit":
            break

        tcp_client_socket.send(send_data.encode("gbk"))

        # 接收对方发送过来的数据，最大接收1024个字节
        recvData = tcp_client_socket.recv(1024)
        print('接收到的数据为:', recvData.decode('gbk'))

    # 关闭套接字
    tcp_client_socket.close()
    ```

    服务器:

    ```python
    from socket import *
    import time

    # 创建socket
    tcp_server_socket = socket(AF_INET, SOCK_STREAM)

    # 本地信息
    address = ('', 7788)

    # 绑定
    tcp_server_socket.bind(address)

    # 使用socket创建的套接字默认的属性是主动的，使用listen将其变为被动的，这样就可以接收别人的链接了
    tcp_server_socket.listen(128)


    client_socket, clientAddr = tcp_server_socket.accept()
    while True:
        # 接收对方发送过来的数据
        recv_data = client_socket.recv(1024).decode('gbk')  # 接收1024个字节
        if len(recv_data) == 0:
            print("程序结束")
            break
        if "你好" in recv_data or "hello" in recv_data:
            client_socket.send("你好".encode('gbk'))
        if "名字" in recv_data or "name" in recv_data:
            client_socket.send("我是Python机器人".encode('gbk'))
        if "时间" in recv_data or "time" in recv_data:
            client_socket.send("当前时间是：%s".encode('gbk')%time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

    # 关闭为这个客户端服务的套接字，只要关闭了，就意味着为不能再为这个客户端服务了，如果还需要服务，只能再次重新连接
    client_socket.close()
    ```

    ​