from collections import defaultdict
import time

def optimal_cost(weigts):
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


def print_matrix(matrix, n):
	for i in range(1, n+1):
		for j in range(1, n+1):
			print('{0:8d}'.format(matrix[(i,j)]), end=' ')
		print()

if __name__ == '__main__':
	b = time.time()
	n = int(input())
	weights = list(map(int, input().split()))
	m, s = optimal_cost(weights)
	print('optimal cost:', m[(1, n-1)])
	print('total run time:', time.time() - b)
	#print('optimal solution: ', optimal_solution(s, 1, n-1))
	#print_matrix(m, n)
	#print_matrix(s, n)