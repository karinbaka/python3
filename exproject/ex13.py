#!/usr/bin/env python
from sys import argv
#read the WYSS section for how to run this

script , first , second , third = argv

#获取script，argv[1]表示第一个参数，0是脚本文件名路径  print(argv[0]) print(argv[1])
print("The script is called:" , script)
#获取参数
print("Your first variable is:" , first)
print("Your second variable is:" , second)
print("Your third variable is:" , third)
