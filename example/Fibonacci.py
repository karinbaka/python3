nterms = int(input('please input you need number:>  '))

n0 = 0
n1 = 1
count =2

if nterms <= 0:
	print("input numberber")
elif nterms == 1:
	print('Fibonacci:')
	print(n0)
else:
	print('Fibonacci')
	print(n0, ',', n1, end = ',')
	while count < nterms:
		nth = n0 + n1
		print(nth, end = ',')
		n0 = n1
		n1 = nth
		count += 1