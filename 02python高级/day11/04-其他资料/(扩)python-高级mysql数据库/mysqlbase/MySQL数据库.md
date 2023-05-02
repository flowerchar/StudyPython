# MySQL数据库

**学习目标**

* 能够知道MySQL数据库的安装

---

### 1. MySQL数据库的介绍

MySQL是一个关系型数据库管理系统，在 WEB 应用方面，MySQL是最好的 RDBMS \(Relational Database Management System，关系数据库管理系统\) 应用软件，它是由瑞典MySQL AB 公司开发，目前属于 Oracle 旗下产品，MySQL 是最流行的关系型数据库管理系统中的一个。

**MySQL的特点:**

1. MySQL是开源的，所以你不需要支付额外的费用。
2. MySQL支持大型的数据库。可以处理拥有上千万条记录的大型数据库。
3. MySQL使用标准的SQL数据语言形式。
4. MySQL可以安装在不同的操作系统，并且提供多种编程语言的操作接口。这些编程语言包括C、C++、Python、Java、Ruby等等。

### 2. MySQL数据库的安装

* MySQL数据库服务端软件的安装
* MySQL数据库客户端软件的安装

**MySQL数据库服务端软件的安装:**

在Ubuntu中打开终端，输入下面的命令:

```
sudo apt-get install mysql-server
```

**说明:**

* 目前大家使用的Ubuntu中已经安装好了MySQL服务端软件，无需再安装。

**显示MySQL服务端安装包信息效果图:**

![MySQL服务端安装包信息](/mysqlbase/imgs/mysql服务端软件安装包信息.png)

**查看MySQL服务效果图:**

![MySQL服务端安装包信息](/mysqlbase/imgs/mysql服务.png)

**ps说明**

* ps 查看当前系统中的进程
* -a 表示所有用户
* -u 表示显示用户名
* -x 表示显示所有的执行程序

**查看MySQL服务状态:**

```
sudo service mysql status
```

**停止MySQL服务:**

```
sudo service mysql stop
```

**启动MySQL服务:**

```
sudo service mysql start
```

**重启MySQL服务:**

```
sudo service mysql restart
```

**MySQL配置文件的介绍:**

配置文件路径为: /etc/mysql/mysql.conf.d/mysqld.cnf

**查看MySQL配置文件效果图:**

![查看mysql配置文件](/mysqlbase/imgs/查看mysql配置文件.png)

**主要配置信息说明:**

```
port表示端口号，默认为3306

bind-address表示服务器绑定的ip，默认为127.0.0.1

datadir表示数据库保存路径，默认为/var/lib/mysql

log_error表示错误日志，默认为/var/log/mysql/error.log
```

**MySQL数据库客户端软件的安装:**

客户端是程序员或者dba使用的软件，通过socket方式与服务端程序通信。

常用的MySQL数据库客户端软件有

1. 图形化界面客户端Navicat
2. 命令行客户端mysql

**图形化界面客户端Navicat的使用**

1. 可以到[Navicat官网下载](https://www.navicat.com.cn/download/navicat-for-mysql)
2. 将压缩文件拷贝到Ubuntu虚拟机中，放到桌面上，解压

**Navicat的使用说明:**

```
tar zxvf navicat112_mysql_cs_x64.tar.gz

./start_navicat
```

**启动效果图:**

![Navicat启动效果图](/mysqlbase/imgs/navicat启动.png)

**说明:**

点击两次“取消”按钮, 不需要进行安装。

**试用效果图**

![Navicat试用效果图](/mysqlbase/imgs/navicat试用.png)

**启动后效果图**

![Navicat试用效果图](/mysqlbase/imgs/navicat首页.png)

**试用过期的解决办法:**

当过期后，删除用户主目录下的.navicat64目录，继续再使用14天。

```
cd ~
rm -r .navicat64
```

**命令行客户端mysql的安装**

在Ubuntu中打开终端，输入下面的命令:

```
sudo apt-get install mysql-client
```

**说明:**

* 目前大家使用的Ubuntu中已经安装好了MySQL命令行客户端软件，无需再安装。

**显示MySQL客户端安装包信息效果图:**

![MySQL客户端安装包信息](/mysqlbase/imgs/mysql客户端软件安装包信息.png)

**mysql命令的使用帮助:**

```
mysql --help
```

**MySQL客户端的使用:**

MySQL客户端连接MySQL服务端命令

```
mysql -uroot -p
```

**连接效果图:**

![mysql连接操作](/mysqlbase/imgs/mysql连接操作.png)

**说明:**

* -u: 表示MySQL服务端的用户名
* -p: 表示MySQL服务端的密码
* quit 或者 exit 或者 ctr + d 表示退出

### 3. 小结

* MySQL是一个关系型数据库管理系统
* 安装MySQL服务端软件使用: sudo apt-get install mysql-server
* 安装MySQL客户端软件使用: sudo apt-get install mysql-client
* 图形化MySQL客户端软件使用Navicat



