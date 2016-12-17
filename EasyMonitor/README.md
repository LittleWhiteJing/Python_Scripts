# EasyMonitor

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
使用flask和highcharts编写的服务器内存监控系统
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

## 项目说明

 * templates:前台模板文件夹，将内存信息可视化为HTML文件。

 * flask_app.py:后台路由文件，定义相关的路由匹配规则。

 * monitor.py:数据采集文件，读取内存信息并存入数据库。

## 工作原理

 * 使用monitor.py定时获取服务器内存信息并存入数据库。

 * 使用index.html作为前端页面，使用ajax定期向服务器发送请求。

 * 使用flask_app.py做web服务处理，响应用户请求并返回数据。

## 项目部署

 * 在服务器上创建数据库memory和表memory,表中只要两个字段memory和time，一个用于存放内存大小，另一个用于存放对应的时间戳。

 * 运行monitor.py将内存信息存入MySQL数据库中。

 * 运行flask_app.py启动web服务。

 * 打开浏览器，输入服务器ip和端口即可实时获取服务器内存的使用信息。
