import time

def index_min(a, i, j):
	MIN, ans = float('inf'), 0
	k = (i+1)%len(a)
	while k != j:
		if a[k] < MIN:
			ans, MIN = k, a[k]
		k = (k+1)%len(a)
	return ans

# search for all bridges in a and store the min on each bridge
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
		if weights[i] <= weights[j]:
			P1 = optimal(weights, bridges, w3, j, i) if (w3,j,i) not in M else M[(w3,j,i)]
			P2 = optimal(weights, bridges, i, w3, w3) if (i,w3,w3) not in M else M[(i,w3,w3)]
		else:
			P1 = optimal(weights, bridges, i, w3, j) if (i,w3,j) not in M else M[(i,w3,j)]
			P2 = optimal(weights, bridges, w3, j, j) if (w3,j,k) not in M else M[(w3,j,j)]
		M[(i,j,k)] = P1 + P2
		return M[(i,j,k)]
	else:
		w4 = bridges[(i,j)]
		P1 = optimal(weights, bridges, i, w4, k) if (i,w4,k) not in M else M[(i,w4,k)]
		P2 = optimal(weights, bridges, w4, j, k) if (w4,j,k) not in M else M[(w4,j,k)]
		P3 = optimal(weights, bridges, i, j, j) if (i,j,j) not in M else M[(i,j,j)]
		M[(i,j,k)] = min(P1 + P2, weights[i] * weights[k] * weights[j] + P3)
		return M[(i,j,k)]

def optimal_cost(weights):
	global M
	M = {}

	i = weights.index(min(weights))
	weights = weights[i:] + weights[:i]

	w1 = weights.index(min(weights))
	w2 = index_min(weights, w1, w1)

	bridges = find_bridges(weights)

	optimal(weights, bridges, w1, w2, w2) 
	optimal(weights, bridges, w2, w1, w1)

	return M[(w1,w2,w2)] + M[(w2,w1,w1)]

if __name__ == '__main__':
	b = time.time()
	n = int(input())
	weights = list(map(int, input().split()))
	cost = optimal_cost(weights)
	print('optimal cost:', cost)
	print('total run time:', time.time() - b)

