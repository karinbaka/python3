from sys import argv
'''
print(argv[0])
print(argv[1])


script , user_name = argv
prompt = '> '

print(f"Hi {user_name} i'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

script, filename = argv
txt = open(filename)
print(txt.read())
'''
'''
txt = open('./pymysql的方法', mode='r', encoding='utf8')
#print(txt.read())
txt.close()

mysql_config = open('./my.cnf',mode='a+')
mycnf = """
[mysqld]
log_error = /data/mysql/logs/error.log
server-id = 1
log_bin = /data/mysql/logs/mysql-bin.log
expire_logs_days = 10
max_binlog_size = 100M
binlog_do_db = include_database_name
binlog_ignore_db = include_database_name
"""
print(mycnf)
mysql_config.write(mycnf)
mysql_config.close()
'''

mysql_config = open('./my.cnf', mode='a+')
mycnf = """
[mysqld]
log_error = /data/mysql/logs/error.log
server-id = 1
log_bin = /data/mysql/logs/mysql-bin.log
expire_logs_days = 10
max_binlog_size = 100M
binlog_do_db = include_database_name
binlog_ignore_db = include_database_name
"""
#print(mycnf)
mysql_config.write(mycnf)
mysql_config.close()