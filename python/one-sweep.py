import random

def one_sweep(a):
	n = len(a)
	index = 0
	MIN = a[index]
	for i, e in enumerate(a):
		if MIN > e:
			index = i
			MIN = e
	a = a[index:] + a[:index]

	ret = []
	stack = []
	#reti = []
	#stacki = []
	for i, e in enumerate(a):
		if len(stack) >= 2 and stack[-1] > e:
			stack.pop()
			#stacki.pop()
			ret.append((stack[-1], e))
			#reti.append((stacki[-1], i))
		else:
			stack.append(e)
			#stacki.append(i)
	while len(stack) > 3:
		stack.pop()
		#stacki.pop()
		ret.append((stack[-1], a[0]))
		#reti.append((stacki[-1], 0))

	return ret

def mark_bridges(a):
	n = len(a)
	index = 0
	MIN = a[index]
	for i, e in enumerate(a):
		if MIN > e:
			index = i
			MIN = e
	a = a[index:] + a[:index]

	ret = []
	stack = []
	i = 0
	while True:
		stack.append(a[i])
		i += 1
		while stack[-1] > a[i%n]:
			tmp = stack.pop()
			ret.append((stack[-1], tmp))
			ret.append((tmp, a[i%n]))
		if i == len(a):
			break

	return ret


a = [random.randint(5, 100) for _ in range(10)]
#print a
print one_sweep([75, 43, 32, 87, 81, 95, 43, 79, 87, 37])