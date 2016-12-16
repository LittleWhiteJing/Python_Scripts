#coding=utf-8
import sys, time 
reload(sys) 
sys.setdefaultencoding('utf8')
from flask import Flask, url_for, redirect
from flask import request
from flask import render_template
import pyodbc
app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_world():
    return 'Hello World!'
	
@app.route('/home')
def home():
	cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=127.0.0.1,1433;DATABASE=shopdb;UID=sa;PWD=123;CHARSET=UTF8')
	cursor = cnxn.cursor()
	sql = "select * from shop_goods"
	cursor.execute(sql)
	rows = cursor.fetchall()
	return render_template('home.html',rows = rows)

@app.route('/detail')
def detail():
	goods_id = request.args.get('goods_id')
	cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=127.0.0.1,1433;DATABASE=shopdb;UID=sa;PWD=123;CHARSET=UTF8')
	cursor = cnxn.cursor()
	sql = "select * from shop_goods where id="+goods_id
	cursor.execute(sql)
	row = cursor.fetchone()
	return render_template('detail.html',row = row)
	
@app.route('/login', methods=['POST', 'GET'])
def login():
	error = ""
	url = url_for('login')
	logo = url_for('static', filename='rox.png')
	if request.method == 'POST':
		cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=127.0.0.1,1433;DATABASE=shopdb;UID=sa;PWD=123;CHARSET=UTF8')
		cursor = cnxn.cursor()
		cursor.execute("select * from shop_user")
		info = cursor.fetchone();
		if request.form['username']==info.username and request.form['password']==info.password:
			return redirect(url_for('index'))
		else:
			msg = "用户名或密码错误!"
			time = 3
			url = url_for('login')
			return render_template('message.html',data=[msg,time,url])
	return render_template('sigin.html',data=[logo,url])
	
@app.route('/index')
def index():
	cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=127.0.0.1,1433;DATABASE=shopdb;UID=sa;PWD=123;CHARSET=UTF8')
	cursor = cnxn.cursor()
	cursor.execute("select * from shop_goods")
	rows = cursor.fetchall()
	return render_template('admin.html',rows=rows)

@app.route('/add')
def add():
	return render_template('add.html')

@app.route('/insert', methods=['POST', 'GET'])
def insert():
	if request.method == 'POST':
		goods_num = request.form['goods_num'].decode('utf-8')
		goods_name = request.form['goods_name'].decode('utf-8')
		goods_tag = request.form['goods_tag'].decode('utf-8')
		goods_price = request.form['goods_price']
		goods_total = request.form['goods_total']
		f = request.files['goods_img']
		goods_img = "/static/"+f.filename
		f.save("D:\\webapp\\static\\"+f.filename)
		cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=127.0.0.1,1433;DATABASE=shopdb;UID=sa;PWD=123;CHARSET=UTF8')
		cursor = cnxn.cursor()
		sql = "insert into shop_goods(goods_num,goods_name,goods_tag,goods_img,goods_price,goods_total) values ("+goods_num+",'"+goods_name+"','"+goods_tag+"','"+goods_img+"',"+goods_price+",'"+goods_total+"')"
		cursor.execute(sql.encode('gbk'))
		cursor.commit()
		msg = "添加成功!"
		time = 3
		url = url_for('index')
		return render_template('message.html',data=[msg,time,url])
	
@app.route('/edit', methods=['POST', 'GET'])
def edit():
	goods_id = request.args.get('goods_id')
	cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=127.0.0.1,1433;DATABASE=shopdb;UID=sa;PWD=123;CHARSET=UTF8')
	cursor = cnxn.cursor()
	sql = "select * from shop_goods where id="+goods_id
	cursor.execute(sql)
	row = cursor.fetchone()
	return render_template('edit.html',row = row)

@app.route('/update', methods=['POST', 'GET'])
def update():
	if request.method == 'POST':
		goods_id = request.form['goods_id']
		goods_num = request.form['goods_num'].decode('utf-8')
		goods_name = request.form['goods_name'].decode('utf-8')
		goods_tag = request.form['goods_tag'].decode('utf-8')
		goods_price = request.form['goods_price']
		goods_total = request.form['goods_total']
		f = request.files['goods_img']
		goods_img = "/static/"+f.filename
		f.save("D:\\webapp\\static\\"+f.filename)
		cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=127.0.0.1,1433;DATABASE=shopdb;UID=sa;PWD=123;CHARSET=UTF8')
		cursor = cnxn.cursor()
		sql = "update shop_goods set goods_num='"+goods_num+"',goods_name='"+goods_name+"',goods_tag='"+goods_tag+"',goods_img='"+goods_img+"',goods_price="+goods_price+",goods_total="+goods_total+" where id="+goods_id 
		cursor.execute(sql.encode('gbk'))
		cursor.commit()
		msg = "修改成功!"
		time = 3
		url = url_for('index')
		return render_template('message.html',data=[msg,time,url])

@app.route('/delete',methods=['POST', 'GET'])
def delete():
	goods_id = request.args.get('goods_id')
	cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=127.0.0.1,1433;DATABASE=shopdb;UID=sa;PWD=123;CHARSET=UTF8')
	cursor = cnxn.cursor()
	sql	= "delete from shop_goods where id="+goods_id
	cursor.execute(sql)
	cursor.commit()
	msg = "删除成功!"
	time = 3
	url = url_for('index')
	return render_template('message.html',data=[msg,time,url])

@app.route('/search',methods=['POST', 'GET'])
def search():
	if request.method == 'POST':
		keywords = request.form['keywords']
		sign = request.form['sign']
		cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=127.0.0.1,1433;DATABASE=shopdb;UID=sa;PWD=123;CHARSET=UTF8')
		cursor = cnxn.cursor()
		sql = "select * from shop_goods where goods_name like '%"+keywords+"%'"
		cursor.execute(sql)
		rows = cursor.fetchall()
		if(sign == 0):
			return render_template('admin.html', rows = rows)
		else:
			return render_template('home.html', rows = rows)
if __name__ == '__main__':
    app.run()