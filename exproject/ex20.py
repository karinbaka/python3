#!/usr/bin/env python
from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())
#移动文件指针，0偏移量，第二个参数默认为0可不填，0，从头开始 1，从当前位置开始 2.从文件末尾
def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)
#重写current_line
current_line = current_line + 1
print_a_line(current_line, current_file)
#重写current_line
current_line = current_line + 1
print_a_line(current_line, current_file)
