#!/usr/local/env python
# -*- coding:utf-8 -*-

#####
#
#
#####

import os
import sys

if os.getuid() == 0:
    pass
else:
    print("需要root用户才可以安装")
    sys.exit(1)
#安装依赖：
yilai = 'yum install -y gcc gcc-c++ openssl openssl-devel ncurses ncurses pcre zlib zlib-devel pcre-devel libtool automake autoconf curl curl-devel libjpeg libjpeg-devel libpng libpng-devel freetype freetype-devel libxslt libxslt-devel bzip2 bzip2-devel openldap openldap-devel libffi-devel'
res = os.system(yilai)

#安装python3:

url = 'https://www.python.org/ftp/python/3.7.1/Python-3.7.1.tgz'
cmd = 'wget ' + url

package_version = url.split('/')[-1]

package_dir = package_version[0:len(package_version)-4]

#判断是否存在python的包，如果存在则不下载：
if os.path.isfile(package_version) == 1:
    pass
else:
    res = os.system(cmd)
    if res != 0:
        print("无法下载python源码包，请确认网络正常！")
        sys.exit(1)

cmd = 'tar zxvf ' + package_version

#判断是否已经解压：
if os.path.exists(package_dir) == 1:
    pass
else:
    res = os.system(cmd)

cmd = 'cd ' + package_dir + \
    ' && ./configure --prefix=/usr/local/python && make && make install'
if os.path.exists('/usr/local/python') == 1:
    print("/usr/local/python目录存在，跳过编译安装！")
    pass
else:
    res = os.system(cmd)
    if res != 0:
        print('编译错误,请检查依赖重新编译!')
        sys.exit(1)

#创建软链接：
cmd = 'ln -s /usr/local/python/bin/pip3 /usr/bin/pip3 && ln -s /usr/local/python/bin/python3 /usr/bin/python3'
res = os.system(cmd)

if res != 0:
    print('无法创建软链接，检查目录下是否存在')
    sys.exit(1)
else:
    print('Python3 安装完成!')

#更新pip
cmd = 'pip3 install --upgrade pip && pip3 -V && python3 -V'
res = os.system(cmd)

#Nginx 安装:

url = 'http://nginx.org/download/nginx-1.14.2.tar.gz'
cmd = 'wget ' + url

nginx_package = url.split('/')[-1]

nginx_dir = nginx_package[0:len(nginx_package)-7]

#下载nginx源码包:
if os.path.isfile(nginx_package) == 1:
    print("nginx为已存在的包，无需下载！")
    pass
else:
    res = os.system(cmd)
    if res != 0:
        print("下载失败，请检查网络！")
        sys.exit(1)

cmd = 'tar zxvf ' + nginx_package

if os.path.exists(nginx_dir) == 1:
    print('该文件已经解压，无需再次减压！')
    pass
else:
    res = os.system(cmd)

cmd = 'cd ' + nginx_dir + \
    ' && ./configure --prefix=/usr/local/nginx && make && make install'

if os.path.exists('/usr/local/nginx'):
    print("/usr/local/nginx目录已经存在，跳过编译安装！")
    pass
else:
    res = os.system(cmd)
    if res != 0:
        print("编译失败，请重新执行！")
        sys.exit(1)
    else:
        print("nginx安装完成！")


#Mysql安装
url = 'https://cdn.mysql.com//Downloads/MySQL-5.7/mysql-5.7.24-linux-glibc2.12-x86_64.tar'
cmd = 'wget ' + url

mysql_package = url.split('/')[-1]
mysql_dir = mysql_package[0:len(mysql_package)-4]

if os.path.isfile(mysql_package):
    print("mysql包已存在，无需下载！")
    pass
else:
    res = os.system("cmd")
    if res != 0:
        print("下载失败，请检查网络！")
        sys.exit(1)

cmd = 'tar zxvf ' + mysql_package + ' -C /usr/loca/mysql'

