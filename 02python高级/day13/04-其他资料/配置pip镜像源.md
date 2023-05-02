# 配置pip国内镜像

## windows

```
1. 进入C:\Users\你的用户名 目录
2. 新建pip文件夹，进到文件夹中创建pip.ini文件
3. 在pip.ini文件中输入


[global]
index-url = https://mirror.baidu.com/pypi/simple
[install]
trusted-host = https://mirror.baidu.com/pypi
```

## mac

```
1. 进入用户目录      cd ~
2. 创建.pip文件夹    mkdir .pip
3. 进入.pip文件夹    cd .pip  
4. 创建pip.conf文件  touch pip.conf  
5. 编辑pip.conf文件  vim pip.conf   

[global]
index-url = https://mirror.baidu.com/pypi/simple
[install]
trusted-host = https://mirror.baidu.com/pypi
```

## ubuntu

```
linux配置

1. mkdir ~/.pip
2. cd ~/.pip
3. touch pip.conf
4. sudo gedit ~/.pip/pip.conf
5. 添加镜像源

[global]
index-url = https://mirror.baidu.com/pypi/simple
[install]
trusted-host = https://mirror.baidu.com/pypi
```

# 安装库

1. windows

   ```bash
   pip install 库
   ```

2. ubuntu

   ```bash
   pip3 install 库
   ```

3. mac

   ```bash
   pip3 install 库
   ```

   

