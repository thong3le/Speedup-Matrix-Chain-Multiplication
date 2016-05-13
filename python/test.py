from collections import defaultdict
import random, time

def optimal_cost(weights):
	# find number of matrices
	n = len(weights) - 1
	# create memoization cost-matrix m and solution matrix s
	m, s = defaultdict(int), defaultdict(int)
	for d in range(1, n):
		for i in range(1, n-d+1):
			j = i+d
			m[(i,j)] = float('inf')
			for k in range(i, j):
				cost = m[(i, k)] + m[(k+1, j)] + weights[i-1] * weights[k] * weights[j]
				if cost < m[(i,j)]:
					m[(i,j)] = cost
					s[(i,j)] = k
	return m, s

def optimal_solution(s, i, j):
	return "A" + str(j) if i == j else "(" + get_optimal(s, i, s[(i, j)]) + get_optimal(s, s[(i,j)] + 1, j) + ")"

def normal_dp(weights):
	m, s = optimal_cost(weights)
	return m[(1, len(weights)-1)]

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

def speedup_topdown(weights):
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

def test():
	for tc in range(100):
		a = [random.randint(100, 100) for _ in range(100)]
		cost1, cost2 = normal_dp(a), speedup_topdown(a)
		if (cost1 != cost2):
			print(cost1, cost2, a)
			break
		else:
			print('pass', tc)

def main():
	n = int(input())
	weights = list(map(int, input().split()))
	cost = speedup_topdown(weights)
	print('optimal cost:', cost)

if __name__ == '__main__':
	b = time.time()
	test()
	print('total run time:', time.time() - b)

#n = int(input())
#a = list(map(int, input().split()))

#cost = solve(a)
#print(cost)
#for k,v in M.items():
#	print(k, v)
