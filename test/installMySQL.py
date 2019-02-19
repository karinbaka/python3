#!/usr/local/env python
# -*- coding:utf-8 -*-
######
#
# @ Author: kainrbaka
# @ email: 47525620@qq.com
#
######
#MySQL安装5.7.24 编译太麻烦了也费时间，直接下载使用的二进制包
import os
import sys


url = 'https://cdn.mysql.com//Downloads/MySQL-5.7/mysql-5.7.24-linux-glibc2.12-x86_64.tar'
cmd = 'wget ' + url

mysql_package = url.split('/')[-1]
#mysql_dir = mysql_package[0:len(mysql_package)-4]

if os.path.isfile(mysql_package):
    print("mysql包已存在，无需下载！")
    pass
else:
    res = os.system(cmd)
    if res != 0:
        print("下载失败，请检查网络！")
        sys.exit(1)

cmd = 'tar xvf ' + mysql_package
mysql_dir = 'mysql-5.7.24-linux-glibc2.12-x86_64.tar.gz'
res = os.system(cmd)

#这个包是解压解包出来的，需要二次解压
cmd = 'tar zxvf '+ mysql_dir +' -C /usr/local/ && \
mv -f /usr/local/'+ mysql_dir[0:len(mysql_dir)-7] +' /usr/local/mysql'

#cmd2 = 'mv -f /usr/local/'+ mysql_dir[0:len(mysql_dir)-7] +' /usr/local/mysql'

if os.path.exists('/usr/local/'+ mysql_dir[0:len(mysql_dir)-7]) == 1:
    print("已经解压在当前路径！")
    pass
elif os.path.exists('/usr/local/mysql') == 1:
    print("路径下已经存在mysql目录，请检查路径！")
    pass
else:
    res = os.system(cmd)

if os.path.exists('/data/mysql/data') == 1:
    pass
else:
    print("需要创建路径!")
    os.makedirs('/data/mysql/data/')

if os.path.exists('/data/mysql/logs') == 1:
    pass
else:
    print("需要创建路径！")
    os.makedirs('/data/mysql/logs/')
    print("目录创建完成！")

#安装mysql
#if os.path.exists('/usr/logs/mysql/') == 1:
#    print("已经安装的mysql，目录已经存在！")
#    pass
#else:
#    res = os.system(cmd2)

#配置my.cnf:
mysql_config = open('/etc/my.cnf', mode='w')
mycnf = """
[mysqld]
port = 8010
basedir = /usr/local/mysql/
datadir = /data/mysql/data/
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


#加入环境变量：
cmd = "echo 'export PATH=/usr/local/mysql/bin:/usr/local/mysql/lib:$PATH' >> /etc/profile && source /etc/profile"
res = os.system(cmd)

#创建用户，组：
cmd = 'groupadd mysql && useradd -r -g mysql -s /bin/false -M mysql'
res = os.system(cmd)

#添加service启动mysqld：
cmd = 'cp -a /usr/local/mysql/support-files/mysql.server /etc/init.d/mysqld && chmod a+x /etc/init.d/mysqld'
res = os.system(cmd)

#改变文件所有者：
cmd = 'chown mysql.mysql -R /usr/local/mysql && chown mysql.mysql -R /data/mysql/'
res = os.system(cmd)

#初始化并启动：
cmd = 'mysqld --initialize --user=mysql && service mysqld start && cat /data/mysql/logs/error.log |grep password'
res = os.system(cmd)

print("""
    请依次输入如下内容完成密码修改：
    mysql -uroot -p
    1.设置密码：
    set password=password('123456');
    2.特定ip访问mysql ip可以用%号表示全部可以访问：
    GRANT ALL PRIVILEGES ON *.* TO '用户'@'特定IP' IDENTIFIED BY '密码' WITH GRANT OPTION;
    3.权限刷新：
    flush privileges;
    4.退出
    quit;
    """)
