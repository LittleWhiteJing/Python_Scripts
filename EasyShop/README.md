# EasyShop

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
 使用flask和pyodbc编写的python商店小应用，数据库使用sqlsrv。
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

## 项目说明

* 由于项目数据库使用的是sqlsrv，所以本项目应部署在windows平台上

 * static：前台静态资源文件夹，保存images,css和js等资源。

 * template：模板文件夹，保存前台模板。

 * flask_app.py：flask路由文件，定义url路由规则和相应处理。

 * sqldump.sql：数据库导出文件。

## 项目部署

#### Python环境配置

 * 安装python2.7.6

 下载地址：https://www.python.org/download/releases/2.7.6/

 * 安装setuptools

 下载地址：https://pypi.python.org/pypi/setuptools

 下载后通过命令行运行安装脚本进行安装：python setup.py install

 * 安装pip

 下载地址：https://pypi.python.org/pypi/pip#downloads

 下载后通过命令行运行安装脚本进行安装：python setup.up install

 * 安装pyodbc

 终端输入命令：pip install pyodbc

 * 安装flask

 终端输入命令：pip install flask

 * 验证是否配置成功

 终端下进入python的交互模式，导入pyodbc模块和flask模块，如果无错误回现示为配置成功

#### SQL Server环境配置

 * 安装SQL Server

 * 配置监听ip地址和端口

  打开配置管理器，图形化设置SQL Server的监听ip和port分别为127.0.0.1和1433

 * 配置SQL Server的超级用户和密码

  osql -E 进入命令模式，输入命令：master..sp_password null,'123','sa',将超级用户sa的密码重置为123

 * 在终端下重启SQL Server服务

  终端下输入命令：net stop mssqlserver 提示停止成功后再次输入:net start
mssqlserver

 * 将sqldump.sql导入数据库

  使用sa用户登陆数据库服务器，注意ip和端口，登陆后导入我们的数据库备份文件sqldump.sql

#### Web应用创建

 * 创建应用文件夹

 * 将此目录下的文件全部复制到该文件夹下方

 * 打开终端，输入命令python flask_app.py执行flask_app.py，启动web服务
