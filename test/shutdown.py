import os
#windows
#os.system('shutdown -s -t 0')
#linux
#os.system('shutdown -h now')

url = 'https://www.python.org/ftp/python/3.7.1/Python-3.7.1.tgz'
#version=(url.split('/'))
version = url.split('/')[-1]
#print(version[-1])

cmd = 'tar zxvf '+ version[0:len(version)-4]
print(cmd)

print(os.path.exists("Python-3.7.1.tgz"))
'''
url = 'https://cdn.mysql.com//Downloads/MySQL-5.7/mysql-5.7.24-linux-glibc2.12-x86_64.tar'
cmd = 'wget ' + url
mysql_package = url.split('/')[-1]
mysql_dir = mysql_package[0:len(mysql_package)-4]
print(mysql_package)
print(mysql_dir)
cmd = 'tar zxvf '+ mysql_dir +' -C /usr/local/mysql'
print(cmd)
cmd = 'tar tf ' + mysql_package
print(cmd)
path = "d:/tmp/home/monthly/daily"
print(os.makedirs(path))
'''
mysql_dir = 'mysql-5.7.24-linux-glibc2.12-x86_64.tar.gz'
#cmd = 'tar zxvf '+ mysql_dir +' -C /usr/local/ && mv /usr/local/'+ mysql_dir[0:len(mysql_dir)-7] +' /usr/local/mysql'
cmd = 'mv -f /usr/local/'+ mysql_dir[0:len(mysql_dir)-7] +' /usr/local/mysql'
print(cmd)

#tar zxvf mysql-5.7.24-linux-glibc2.12-x86_64.tar.gz -C /usr/local/

