#!/usr/bin/python
#coding:utf-8
import os 
import sys
 
if os.getuid() == 0:
  pass
else:
  print ('Not under root mode, please switch user!')
  sys.exit(1)

yilai = 'yum install gcc gcc-c++ openssl openssl-devel ncurses ncurses pcre zlib zlib-devel pcre-devel libtool automake autoconf curl curl-devel libjpeg libjpeg-devel libpng libpng-devel freetype freetype-devel libxslt libxslt-devel bzip2 bzip2-devel openldap openldap-devel libffi-devel -y'
res = os.system(yilai)

url = 'https://www.python.org/ftp/python/3.7.1/Python-3.7.1.tgz'
cmd = 'wget ' + url
res = os.system(cmd)
if res != 0 :
  print ('Failed to download python source package, please inspect your network!')
  sys.exit(1)

#package_version = 'Python-3.7.1'
package_version = url.split('/')[-1]

cmd = 'tar zxvf '+ package_version
res = os.system(cmd)
 
#if res != 0:
#  os.system('rm ' + package_version + '.tgz')
#  print 'Please reexcute the script to install python'
#  sys.exit(1)
 

cmd = 'cd ' + package_version + ' && ./configure --prefix=/usr/local/python && make && make install'
 
res = os.system(cmd)
 
if res != 0:
  print ('Failed to install python!')
  sys.exit(1)

cmd = 'ln -s /usr/local/python/bin/pip3 /usr/bin/pip3 && ln -s /usr/local/python/bin/python3 /usr/bin/python3'
res = os.system(cmd)
if res != 0:
  print ('Unable to create link！')
  sys.exit(1)
else:
  print('Python3 install success!')
#Nginx


url = 'http://nginx.org/download/nginx-1.14.2.tar.gz'
cmd = 'wget ' + url
res = os.system(cmd)
if res != 0 :
  print ('Failed to download nginx source package, please inspect your network!')
  sys.exit(1)

nginx_package_version = url.split('/')[-1]
#nginx_package_version = 'nginx-1.14.2'

cmd = 'tar zxvf '+ nginx_package_version
res = os.system(cmd)

cmd = 'cd ' + nginx_package_version + ' && ./configure --prefix=/usr/local/nginx && make && make install'
res = os.system(cmd)
if res != 0:
  print ('Failed to install nginx!')
  sys.exit(1)
else:
  print('install python3 and nginx success')

