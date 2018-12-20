import os
import sys
import re
#windows
#os.system('shutdown -s -t 0')
#linux
#os.system('shutdown -h now')
'''
url = 'https://www.python.org/ftp/python/3.7.1/Python-3.7.1.tgz'
#version=(url.split('/'))
version = url.split('/')[-1]
#print(version[-1])

cmd = 'tar zxvf '+ version[0:len(version)-4]
print(cmd)

print(os.path.exists("Python-3.7.1.tgz"))
'''
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
'''
mysql_dir = 'mysql-5.7.24-linux-glibc2.12-x86_64.tar.gz'
#cmd = 'tar zxvf '+ mysql_dir +' -C /usr/local/ && mv /usr/local/'+ mysql_dir[0:len(mysql_dir)-7] +' /usr/local/mysql'
cmd = 'mv -f /usr/local/'+ mysql_dir[0:len(mysql_dir)-7] +' /usr/local/mysql'
print(cmd)

#tar zxvf mysql-5.7.24-linux-glibc2.12-x86_64.tar.gz -C /usr/local/
url = 'http://101.96.10.63/cn2.php.net/distributions/php-7.3.0.tar.bz2'
php_package = url.split('/')[-1]
php_dir = php_package[0:len(php_package)-8]
cmd = 'tar jxvf ' + php_package
print(cmd)

cmd = 'cd ' + php_dir + ' && ./configure --prefix=/usr/local/php7.3  \
--with-curl --with-freetype-dir --with-gd --with-gettext --with-iconv-dir \
--with-kerberos --with-libdir=lib64 --with-libxml-dir --with-mysqli --with-openssl \
--with-pcre-regex --with-pdo-mysql --with-pdo-sqlite --with-pear --with-png-dir \
--with-jpeg-dir --with-xmlrpc --with-xsl --with-zlib --with-bz2 --with-mhash \
--enable-fpm --enable-bcmath --enable-libxml --enable-inline-optimization \
--enable-gd-native-ttf --enable-mbregex --enable-mbstring --enable-opcache \
--enable-pcntl --enable-shmop --enable-soap --enable-sockets \
--enable-sysvsem --enable-sysvshm --enable-xml --enable-zip'
print(cmd)

'''

url = 'https://github-production-release-asset-2e65be.s3.amazonaws.com/537699/1da94100-feb4-11e8-9c6d-90a17b15381a?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20181220%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20181220T063003Z&X-Amz-Expires=300&X-Amz-Signature=512fe7cd95070860349649ad30271d5d367eaaca706e4a293df63dad6353b50c&X-Amz-SignedHeaders=host&actor_id=21166528&response-content-disposition=attachment%3B%20filename%3Dcmake-3.13.2.tar.gz&response-content-type=application%2Foctet-stream'
cmd = 'wget ' + url


cmake_package = re.findall(r"3D(.+?)&", url)
cmake_package = ' '.join(cmake_package)
cmake_dir = cmake_package[0:len(cmake_package)-7]
print(cmake_dir)
url = 'https://cmake.org/files/v3.12/cmake-3.12.4-Linux-x86_64.tar.gz'
cmd2 = 'wget ' + url

#cmake_package = re.findall(r"3D(.+?)&", url)
cmake_package = url.split('/')[-1]
cmake_dir = cmake_package[0:len(cmake_package)-7]
print(cmd2)
print(cmake_dir)
dirname = 'tar zxvf ' + cmake_package + ' -C /usr/local/ && mv /usr/local/' + cmake_dir + ' /usr/local/camke'
print(dirname)


libzip_package = url.split('/')[-1]
libzip_dir = libzip_package[0:len(libzip_package)-7]

cmd = 'tar zxvf ' + libzip_package + ' -C /usr/local/ && mv /usr/local/' + libzip_dir + ' /usr/local/libzip \
&& cd /usr/local/libzip && mkdir build && cd build && cmake .. && make && make install'
print(cmd)