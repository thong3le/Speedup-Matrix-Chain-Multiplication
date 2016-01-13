import sys, time, random
LIMIT = 10**3
MAX = sys.maxint
M = [[MAX]*LIMIT for _ in range(LIMIT)]
S = [[-1]*LIMIT for _ in range(LIMIT)]

def string_cut(n, cuts):

    M = [[MAX]*LIMIT for _ in range(LIMIT)]
    S = [[-1]*LIMIT for _ in range(LIMIT)]

    p = [0] + cuts + [n]
    return memoized_string_cut(p, 0, len(p) - 1)

def memoized_string_cut(p, i, j):
    if M[i][j] < MAX:
        return M[i][j]
    if i == j-1:
        M[i][j] = 0
        return 0
    for k in range(i+1, j):
        q = memoized_string_cut(p, i, k) + memoized_string_cut(p, k, j) + p[j] - p[i]
        if q < M[i][j]:
            M[i][j] = q
            S[i][j] = k
    return M[i][j]

def get_optimal(i, j):
    if i == j-1:
        return []
    else:
        return [S[i][j]] + get_optimal(i, S[i][j]) + get_optimal(S[i][j], j)

def get_optimal_parentheses(i, j):
    if i == j-1:
        return "A" + str(j)
    else:
        return "(" + get_optimal_parentheses(i, S[i][j]) + get_optimal_parentheses(S[i][j], j) + ")" 

def run_testcases(tc = 10):
    n = 20
    for _ in range(tc):
        tmp = random.randint(4, 7)
        cuts = {}
        for _ in range(tmp):
            cuts[random.randint(1, n-1)] = 0
        cuts = cuts.keys()
        cuts.sort()
        print "String has length {} and the number of cuts are {}".format(n, len(cuts))
        print [0] + cuts + [n]
        print "Optimal cost: ", string_cut(n, cuts)
        print "Optimal cut order:", get_optimal(0, len(cuts)+1)
        print get_optimal_parentheses(0, len(cuts)+1)
        
        print 

def example():
    n = 20
    cuts = [3, 5, 6, 12, 14]
    print cuts 
    print string_cut(n, cuts)

    print "Optimal cut order:", get_optimal(0, len(cuts)+1)
    print get_optimal_parentheses(0, len(cuts)+1)

def main():
    
    example()

    #run_testcases(5)
    

if __name__ == '__main__':
    b = time.time()
    main()
    print 'total run time is:', time.time()-b