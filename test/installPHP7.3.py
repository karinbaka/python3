#!/usr/local/env python
# -*- coding:utf-8 -*-
######
#
# @ Author: kainrbaka
# @ email: 47525620@qq.com
#
######

# ps：编译可以按照自己选择，如果有安装监控需求可以依次全部选择

import os
import sys
import re

#卸载旧版本cmake
cmd = 'yum remove cmake -y'
res = os.system(cmd)
if res != 0:
	print("请手动卸载旧版本cmake！")
	sys.exit(1)
else:
	print("旧版cmake卸载完成。准备安装")


#下载cmake
url = 'https://cmake.org/files/v3.12/cmake-3.12.4-Linux-x86_64.tar.gz'
cmd = 'wget ' + url

#cmake_package = re.findall(r"3D(.+?)&", url)
cmake_package = url.split('/')[-1]
cmake_dir = cmake_package[0:len(cmake_package)-7]

if os.path.isfile(cmake_package) == 1:
	print("cmake包已经存在，无需下载！")
	pass
else:
	res = os.system(cmd)
	if res != 0:
		print("请检查网络环境是否异常！")
		sys.exit(1)

#安装cmake

cmd = 'tar zxvf ' + cmake_package + ' -C /usr/local/ && mv /usr/local/' + cmake_dir + ' /usr/local/cmake'

if os.path.exists('/usr/local/cmake') == 1:
	print("已经存在/usr/local/cmake/目录")
	pass
else:
	print("安装cmake")
	res = os.system(cmd)
	print("cmake 安装完成")

cmd = 'ln -s /url/local/cmake/bin/cmake /usr/bin/cmake' 
			 
if os.path.isfile('/usr/bin/cmake') == 1:
	pass
else:
	res =  os.system(cmd)

#下载libzip
url = 'https://libzip.org/download/libzip-1.5.1.tar.gz'
cmd = 'wget ' + url

libzip_package = url.split('/')[-1]
libzip_dir = libzip_package[0:len(libzip_package)-7]

if os.path.isfile(libzip_package) == 1:
	print("已经存在的libzip包，无需下载！")
	pass
else:
	res = os.system(cmd)
	if res != 0:
		print("网络错误，下载失败")
		sys.exit(1)

#安装libzip
cmd = 'tar zxvf ' + libzip_package + ' -C /usr/local/ && mv /usr/local/' + libzip_dir + ' /usr/local/libzip \
&& cd /usr/local/libzip && mkdir build && cd build && cmake .. && make && make install'

if os.path.exists('/usr/local/libzip/'):
	print("已经存在/usr/local/libzip/目录")
	pass
else:
	print("开始安装libzip！")
	res = os.system(cmd)
	print("libzip安装完成!")



#下载php7.3
url = 'http://101.96.10.63/cn2.php.net/distributions/php-7.3.0.tar.bz2'
cmd = 'wget ' + url

php_package = url.split('/')[-1]
php_dir = php_package[0:len(php_package)-8]

if os.path.isfile(php_package) == 1:
	print("php包已存在，无需下载！")
	pass
else:
	res = os.system(cmd)
	if res != 0:
		print("网络异常，下载失败！")
		sys.exit(1)

cmd = 'tar jxvf ' + php_package

if os.path.exists(php_dir) == 1:
	print('已经解压的php包，无需再次解压！')
	pass
else:
	res = os.system(cmd)
	print("解压完成，准备编译！")

cmd = 'cd ' + php_dir + ' && ./configure --prefix=/usr/local/php7  \
--with-curl --with-freetype-dir --with-gd --with-gettext --with-iconv-dir \
--with-kerberos --with-libdir=lib64 --with-libxml-dir --with-mysqli --with-openssl \
--with-pcre-regex --with-pdo-mysql --with-pdo-sqlite --with-pear --with-png-dir \
--with-jpeg-dir --with-xmlrpc --with-xsl --with-zlib --with-bz2 --with-mhash \
--enable-fpm --enable-bcmath --enable-libxml --enable-inline-optimization \
--enable-gd-native-ttf --enable-mbregex --enable-mbstring --enable-opcache \
--enable-pcntl --enable-shmop --enable-soap --enable-sockets \
--enable-sysvsem --enable-sysvshm --enable-xml --with-snmp --with-gmp --with-ldap \
--with-libzip=/usr/local/libzip && make && make install'

if os.path.exists('/usr/local/php7') == 1:
	print("已经存在的路径，无需重新编译！")
	pass
else:
	res = os.system(cmd)
	if res != 0:
		print("编译失败，请检查依赖环境！")
		sys.exit(1)
	else:
		print("php编译完成！")
