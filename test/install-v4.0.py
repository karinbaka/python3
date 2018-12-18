#!/usr/local/env python
# -*- coding:utf-8 -*-
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

#判断是否存在python的包，如果存在则不下载
if os.path.exists(package_version) == 1:
    pass
else:
    res = os.system(cmd)
    if res != 0:
        print("无法下载python源码包，请确认网络正常！")
        sys.exit(1)


cmd = 'tar zxvf ' + package_version

res = os.system(cmd)

cmd = 'cd ' + package_dir + \
    ' && ./configure --prefix=/usr/local/python && make && make install'

res = os.system(cmd)

if res != 0:
    print('编译错误请检查依赖重新编译')
    sys.exit(1)

cmd = 'ln -s /usr/local/python/bin/pip3 /usr/bin/pip3 && ln -s /usr/local/python/bin/python3 /usr/bin/python3'
res = os.system(cmd)

if res != 0:
    print('无法创建软链接，检查目录下是否存在')
    sys.exit(1)
else:
    print('Python3 安装完成!')

#Nginx 安装，如果有本地包直接指定包名

url = 'http://nginx.org/download/nginx-1.14.2.tar.gz'
cmd = 'wget ' + url

nginx_package = url.split('/')[-1]

nginx_dir = nginx_package[0:len(nginx_package)-7]

if os.path.exists(package_version) == 1:
    pass
else:
    res = os.system(cmd)
    if res != 0:
        print("下载失败，请检查网络")
        sys.exit(1)

cmd = 'tar zxvf ' + nginx_package

res = os.system(cmd)

cmd = 'cd ' + nginx_package + \
    ' && ./configure --prefix=/usr/local/nginx && make && make install'

res = os.system(cmd)
if res != 0:
    print("编译失败，请重新执行")
    os.exit(1)
else:
    print("安装完成！")
