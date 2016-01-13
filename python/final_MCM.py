import sys, time
#gk = lambda i,j: str(i) + ',' + str(j)
MAX = sys.maxint

def memoized_matrix_chain(p):
	n = len(p) - 1
	m =[[MAX]*(n+1)]*(n+1)

	for i in range(1, n+1):
		m[i][i] = 0
	for s in range(1, n):
		for i in range(1, n+1-s):
			j = i + s
			for k in range(i, j):
				q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
	return m[1][n]

def main():
	#p = [30, 35, 15, 5, 10, 20, 25, 5, 16, 34, 28, 19, 66, 34, 78, 55, 23]
	p = [30, 35, 15, 5, 10]
	
	print memoized_matrix_chain(p)
	
if __name__ == '__main__':
	b = time.time()
	main()
	print 'total run time:', time.time() - b