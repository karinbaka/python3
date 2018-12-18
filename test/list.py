'''
#传递参数时候不要使用列表
def foo(num,age=[]):
	age.append(num)
	print("num",num)
	return age
print(foo(1))
print(foo(2))
print(foo(3))


#参数的时候默认都是给定 None，然后根据对象判断是否为空，如果为空再去定义成列表
def foo(num, age=None):
    #if not age:
    if age is None:
        age = []
    age.append(num)
    print("num", num)
    return age
print(foo(1))
print(foo(2))
print(foo(3))


#在一般领域，对正整数 n，如果用 2 到根号 N 之间的所有整数去除，均无法整除，则 n 为质数又叫素数。
import math

num = [] #存放 1-100 之间的素数
for i in range(2, 100):
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            break
    else:
        num.append(i) #根据定义如果都无法正常才加入
for index, i in enumerate(num):
    if index == len(num) - 1:
        print(i)
    else:
        print(i, end=" ")





L = [8,2,50,3]
#print(L[-1])
print(L[1], L[-1], L[0], L[-2])
#升序
print(sorted(L))
print(L)

'''
aList = ['Google', 'Runoob', 'Taobao', 'Facebook']
aList.sort()
print (aList)

aList.reverse()
print(aList)

'''

str = "-";  
#字符串用-分割
seq = ("a", "b", "c");
 # 字符串序列
print (str.join(seq))
'''

a={1:1,2:2,3:3}
#b=[]
#for c in a:
#	b.append(c)
#print(b)

#print(list(a.keys()))


b=list(a.keys())

c=[]
for m in b:
    if str(m).isdigit(): ##检测是否数字
        c.append(m)
c.sort()
print (','.join(str(n) for n in c))

fruits = ['apple', 'oranges', 'pears', 'apricots']
for i in fruits:
	print(i)

e = []
for i in range(0, 6):
	print(i)
	e.append(i)
for i in e:
	print(i)

print(hash('abc'))

##斐波那契数列
a, b = 0, 1
while b < 10000:
	print(b , end = ',')
	a, b = b, a + b
print()