import sys, time
gk = lambda i,j: str(i) + ',' + str(j)
MAX = sys.maxint
m = {}
s = {}
def memoized_matrix_chain(p):
	n = len(p) - 1
	for i in xrange(1, n+1):
		for j in xrange(i, n+1):
			m[gk(i,j)] = MAX
	return lookup_chain(p, 1, n)

def lookup_chain(p, i, j):
	if m[gk(i,j)] < MAX:
		return m[gk(i,j)]
	if i == j:
		m[gk(i,j)] = 0
	else:
		for k in xrange(i, j):
			q = lookup_chain(p, i, k) + lookup_chain(p, k+1, j) + p[i-1]*p[k]*p[j]
			if q < m[gk(i,j)]:
				m[gk(i,j)] = q
				s[gk(i,j)] = k
	return m[gk(i,j)]

def get_optimal_parens(i, j):
	res = ''
	if i == j:
		return "A" + str(j)
	else:
		res += "("
		res += get_optimal_parens(i, s[gk(i, j)])
		res += get_optimal_parens(s[gk(i,j)] + 1, j)
		res += ")" 
		return res


def main():
	p = [30, 35, 15, 5, 10, 20, 25, 5, 16, 34, 28, 19, 66, 34, 78, 55, 23]
	#p = [3,2,4,5]
	
	print memoized_matrix_chain(p)
	print get_optimal_parens(1, len(p)-1)

	for i in range(1, len(p)):
		for j in range(1, len(p)):
			if gk(i,j) in m:
				print "%7d" %m[gk(i,j)],
			else:
				print "%7d" % 0, 
		print '\n'

	print "=============================================="
	for i in range(1, len(p)):
		for j in range(1, len(p)):
			if gk(i,j) in s:
				print "%7d" %s[gk(i,j)],
			else:
				print "%7d" % 0, 
		print '\n'

if __name__ == '__main__':
	b = time.time()
	main()
	print 'total run time:', time.time() - b