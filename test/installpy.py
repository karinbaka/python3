#!/usr/bin/python
#coding:utf-8
import os 
import sys
 
if os.getuid() == 0:
  pass
else:
  print ('Not under root mode, please switch user!')
  sys.exit(1)

cmd = 'tar zxvf '
res = os.system(cmd)
 
if res != 0:
  os.system('rm ' + package_version + '.tgz')
  print 'Please reexcute the script to install python'
  sys.exit(1)
 

cmd = 'cd ' + package_version + ' && ./configure --prefix=/usr/local/python && make && make install'
 
res = os.system(cmd)
 
if res != 0:
  print ('Failed to install python, please inspect dependencies for python install!')
  sys.exit(1)