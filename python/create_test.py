import random

n = 5000
MAX = 50000
with open('input/test5000.txt', 'w') as f:
	#p = [random.randint(1, MAX) for _ in range(n)]
	p = random.sample(range(1, MAX), n)
	f.write(str(len(p)) + '\n')
	f.write(' '.join(map(str, p)))
