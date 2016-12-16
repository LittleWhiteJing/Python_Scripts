# EasyShop

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
 使用flask和pyodbc编写的python应用，数据库使用sqlsrv。
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

## 项目说明

* static：前台静态资源文件夹，保存images,css和js等资源。

* template：模板文件夹，保存前台模板。

* flask_app.py：flask路由文件，定义url路由规则和相应处理。

* sqldump.sql：数据库导出文件。

## 项目部署

#### Python环境配置

 * 安装python2.7.6

 * 安装setuptools

 * 安装pip

 * 安装pyodbc

 * 安装flask

#### SQL Server环境配置

 * 安装SQL Server

 * 设置SQL Server的监听ip和port分别为127.0.0.1和1433

 * 设置SQL Server的超级用户和密码分别为sa和123

 * 重启SQL Server服务

 * 登陆SQL Server将sqldump.sql导入数据库

#### Web应用创建

 * 创建应用文件夹

 * 将此目录下的文件全部复制到该文件夹下方

 * 执行flask_app.py，启动web服务
