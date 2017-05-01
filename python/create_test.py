import random

n = 100000
MAX = 5000
with open('input/testdup.txt', 'w') as f:
	# generate weights which can have duplicates
	weights = [random.randint(1, MAX) for _ in range(n)]
	# generate weights which have no duplicates
	#weights = random.sample(range(1, MAX), n)
	f.write(str(len(weights)) + '\n')
	f.write(' '.join(map(str, weights)))
