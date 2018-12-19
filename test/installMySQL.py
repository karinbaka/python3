#!/usr/local/env python
# *-* coding:utf-8 *-*

#MySQL安装
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
cmd = 'tar zxvf '+ mysql_dir +' -C /usr/local/ && mv /usr/local/'+ mysql_dir[0:len(mysql_dir)-7] +' /usr/local/mysql'
print(cmd)
if os.path.exists('/usr/local/mysql') == 1:
	pass
else:
	print("需要创建路径!")
	os.makedirs('/usr/local/mysql')
	print("目录创建完成！")
	res = os.system(cmd)

cmd = 'groupadd mysql && useradd -r -g mysql -s /bin/false -M mysql && echo "export PATH=/usr/local/mysql/bin:/usr/local/mysql/lib:$PATH" >> /etc/profile && source /etc/profile'
res = os.system(cmd)
cmd = 'cp /usr/local/mysql/support-files/mysql.server /etc/init.d/mysqld && chmod a+x /etc/init.d/mysqld'
res = os.system(cmd)
cmd = 'chown mysql.mysql -R /usr/local/mysql'
res = os.system(cmd)
cmd = 'cd /usr/local/mysql/bin/ && ./mysqld --initialize --user=mysql && service mysqld start'

