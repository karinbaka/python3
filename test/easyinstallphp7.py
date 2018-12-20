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

url = 'http://cn2.php.net/distributions/php-7.2.13.tar.bz2'
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
--enable-sysvsem --enable-sysvshm --enable-xml --enable-zip --with-snmp --with-gmp --with-ldap \
&& make && make install'

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

