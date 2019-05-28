# 支持MarkDown的WIKI系统

## 环境依赖

![](https://img.shields.io/badge/language-python3.6-green.svg)

* django1.11
* pymysql
* mysqlclient
* mysql5.7

## 安装

clone本项目之后,配置/tipsy_wiki/tipsy_wiki/settings.py里的数据库相关配置

1. 建立数据库

`进入mysql终端,创建utf8格式的数据库,名为djangodb`

2. 数据库迁移与数据表创建

进入项目根文件夹

`python3 manage.py makemigrations`

`python3 manage.py migrate`

3. 测试数据导入
   
`python3 manage.py shell`

`>>import createdata`

4. 以开发模式运行,实时显示报错
   
`python3 manage.py runserver 0:8000`

* 推荐使用nginx用于生产环境,具体配置请自行搜索