import pymysql.cursors

conn = pymysql.connect(
	host = 'localhost',
	user = 'root',
	password = '123456',
	db = 'test',
	charset = 'utf8',
	)
try:
	with conn.cursor() as cursor:
		sql = "insert into users (`email`,`password`) values (%s, %s)"
		cursor.execute(sql, ('sql@mysql.org', 'very-nice'))
	conn.commit()

	with conn.cursor() as cursor:
		sql = "select `id`, `email`, `password` from users where `id`=%s"
		cursor.execute(sql, ('1',))
		result = cursor.fetchall()
		print(result)
finally:
	conn.close()