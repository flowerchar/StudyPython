## 1.创建虚拟环境

```
python3 -m venv flask_venv
```
## 2.源项目终端，将所有包写入requirements.txt,便于一步完成安装

```
pip freeze > requirements.txt
```
## 3.云服务器虚拟环境中

```
pip3 install -r requirements.txt
```
## 4.虚拟环境中

```
apt-get install nginx
pip3 install gunicorn
```
## 5.配置nginx

```
cd /etc/nginx/sites_available
cp default default_copy
#备份，避免发生意外
vim default

server {
        listen 80;
        # Make site accessible from http://localhost/
        server_name www.pygod.net;
        location / {
                proxy_pass http://127.0.0.1:8000; # 这里是指向 gunicorn host 的服务地址
                proxy_set_header Host $host;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                # First attempt to serve request as file, then
                # as directory, then fall back to displaying a 404.
                # Uncomment to enable naxsi on this location
                # include /etc/nginx/naxsi.rules
        }
```

## 6.hostswen文件

```
vim /etc/hosts
#添加一行代码
127.0.0.1 www.pygod.net
```
## 7.到项目根目录下运行使用gunicorn运行项目

```
gunicorn -D -w 3 -b 0.0.0.0:8000 manage:app
```

-w后面的数字是进程数

-b后面跟地址与端口

-D后台启动

manage为启动的py文件




