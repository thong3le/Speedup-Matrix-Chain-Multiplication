import time

def index_min(a, i, j):
	MIN, ans = float('inf'), -1
	k = (i+1)%len(a)
	while k != j:
		if a[k] < MIN:
			ans, MIN = k, a[k]
		k = (k+1)%len(a)
	return ans

def index_smaller(a, i, j):
	ans = []
	k = (j+1)%len(a)
	while k != i:
		if a[k] <= a[i] and a[k] <= a[j]:
			ans.append(k)
		k = (k+1)%len(a)
	return ans

# search for all bridges in a and store the cones for each bridge
def find_bridges(a):
	n = len(a)
	B, stack = [], []
	cones = {}
	i = 0
	while i < n:
		stack.append(i)
		i += 1
		while a[stack[-1]] > a[i%n]:
			top = stack.pop()
			cones[(stack[-1], top)] = (index_min(a, stack[-1], top), index_smaller(a, stack[-1], top))
			B.append((stack[-1], top))
			cones[(top, i%n)] = (index_min(a, top, i%n), index_smaller(a, top, i%n))
			B.append((top, i%n))
	return B, cones

def optimal_cost(a):
	n = len(a)
	i = a.index(min(a))
	a = a[i:] + a[:i]
	B, cones = find_bridges(a)
	
	M = {}

	for i,j in B:
		if (i+1)%n == j:
			M[(i,j,i)] = 0
			M[(i,j,j)] = 0
			for k in cones[(i,j)][1]:
				M[(i,j,k)] = a[i] * a[j] * a[k]
		else:
			s = cones[(i,j)][0]
			minson = (i, s)
			maxson = (s, j)
			if a[i] < a[j]:
				M[(i,j,i)] = M[(i,s,i)] + M[(s,j,i)]
			else:
				M[(i,j,j)] = M[(i,s,j)] + M[(s,j,j)]
			
			for k in cones[(i,j)][1]:
				p = i if a[i] < a[j] else j
				M[(i,j,k)] = min(a[i] * a[j] * a[k] + M[(i,j,p)], M[(i,s,k)] + M[(s,j,k)])

	w1 = a.index(min(a))
	w2 = index_min(a, w1, w1)

	return M[(w1, w2, w1)] + M[(w2, w1, w1)]


if __name__ == '__main__':
	b = time.time()
	n = int(input())
	a = list(map(int, input().split()))
	#i = a.index(min(a))
	#a = a[i:] + a[:i]
	#B, cones = find_bridges(a)
	
	cost = optimal_cost(a)
	print('optimal cost:', cost)
	
	print('total run time:', time.time() - b)


