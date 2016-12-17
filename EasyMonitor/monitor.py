import MySQLdb as mysql
import time

db = mysql.connect(user="root",passwd="root",db="memory",host="localhost")
db.autocommit(True)
cur = db.cursor()


def getMem():
	f = open('/proc/meminfo')
	total = int(f.readline().split()[1])
	free = int(f.readline().split()[1])
	avalible = int(f.readline().split()[1])
	buffers = int(f.readline().split()[1])
	cache = int(f.readline().split()[1])
	mem_use = total-free-buffers-cache
	t = time.time()
	sql = "insert into memory (memory,time) values (%s,%s)" % (mem_use/1024,t)
	cur.execute(sql)
while True:
	time.sleep(1)
	getMem()
