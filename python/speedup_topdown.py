import time

def index_min(a, i, j):
	n = len(a)
	MIN = min(a[i+1:j]) if i < j else min((a[i:] + a[:j])[1:])
	ans = []
	k = (i+1)%len(a)
	while k != j:
		if a[k] == MIN:
			ans.append(k)
		k = (k+1)%len(a)
	return ans

def find_bridges(a):
	n = len(a)
	ans, stack = {}, []
	i = 0
	while i < n:
		stack.append(i)
		i += 1
		while a[stack[-1]] > a[i%n]:
			top = stack.pop()
			if (stack[-1] + 1)%n != top:
				ans[(stack[-1], top)] = index_min(a, stack[-1], top)
			if (top + 1)%n != i%n:
				ans[(top, i%n)] = index_min(a, top, i%n)
		if a[stack[-1]] == a[i%n] and stack[-1] != i%n and (stack[-1] + 1)%n != i%n:
			ans[(stack[-1], i%n)] = index_min(a, stack[-1], i%n)
	return ans

def optimal(weights, bridges, i, j, k):
	n = len(weights)
	if (i+1)%n == j:
		M[(i,j,k)] = 0 if k == i or k == j else weights[i] * weights[j] * weights[k]
		return M[(i,j,k)]

	elif k == i or k == j:
		w3 = bridges[(i,j)]
		cost = 0
		pairs = zip([i] + w3, w3 + [j])
		if weights[i] <= weights[j]:
			for p, q in pairs:
				cost += optimal(weights, bridges, p, q, i) if (p,q,i) not in M else M[(p,q,i)]
		else:
			for p, q in pairs:
				cost += optimal(weights, bridges, p, q, j) if (p,q,j) not in M else M[(p,q,j)]

		M[(i,j,k)] = cost
		return M[(i,j,k)]
	else:
		cost1 = weights[i] * weights[k] * weights[j] + (optimal(weights, bridges, i, j, j) if (i,j,j) not in M else M[(i,j,j)])
		cost2 = 0
		w4 = bridges[(i,j)]
		pairs = zip([i] + w4, w4 + [j])
		for p, q in pairs:
			cost2 += optimal(weights, bridges, p, q, k) if (p,q,k) not in M else M[(p,q,k)]
		M[(i,j,k)] = min(cost1,cost2)
		return M[(i,j,k)]

def optimal_cost(weights):
	global M
	M = {}
	i = weights.index(min(weights))
	weights = weights[i:] + weights[:i]
	bridges = find_bridges(weights)

	MIN = min(weights)
	w1 = []
	for i in range(0, len(weights)):
		if weights[i] == MIN:
			w1.append(i)
	cost = 0
	if len(w1) > 1:
		tmp = w1[1:] + [w1[0]]
		pairs = zip(w1, tmp)
		for i, j in pairs:
			cost += optimal(weights, bridges, i, j, j) 
		return cost + (len(w1) - 2) * MIN * MIN * MIN
	else:
		w2  = index_min(weights, w1[0], w1[0])
		pairs = zip(w1 + w2, w2 + w1)
		for i, j in pairs:
			cost += optimal(weights, bridges, i, j, w1[0]) 
		return cost

if __name__ == '__main__':
	b = time.time()
	n = int(input())
	weights = list(map(int, input().split()))
	cost = optimal_cost(weights)
	print('optimal cost:', cost)
	print('total run time:', time.time() - b)
