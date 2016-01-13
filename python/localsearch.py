def update(x, y, u, v):
	if (x,y) in data:
				temp1 = data[(x,y)][0]
				temp2 = data[(x,y)][1]
				if len(set(temp1) - set([x, y, u])) == 0:
					data[(x,y)] = [temp2, (x, y, v)]
				else:
					data[(x,y)] = [temp1, (x, y, v)]

def improved():
	flag = False
	global cost
	for k, v in data.items():
		a, b = k
		c = (set(v[0]) - set(k)).pop()
		d = (set(v[1]) - set(k)).pop()
		delta = 1.0/p[c] + 1.0/p[d] - 1.0/p[a] - 1.0/p[b]
		if delta > 0:
			flag = True
			data.pop(k)
			data[(c,d)] = [(c, d, a),(c, d, b)]
			cost = cost + p[c]*p[d]*p[a] + p[c]*p[d]*p[b] - p[a]*p[b]*p[c] - p[a]*p[b]*p[d]
			update(a, c, b, d)
			update(c, a, b, d)
			update(b, c, a, d)
			update(c, b, a, d)
			update(a, d, b, c)
			update(d, a, b, c)
			update(b, d, a, c)
			update(d, b, a, c)
			break	
	return flag

#p = [0, 141, 135, 189, 116, 105, 160]
#p = [0, 128, 141, 182, 109, 167, 141]
#p = [0, 103, 102, 197, 110, 116, 167]
#p = [0, 119, 143, 111, 130, 108, 117]
#p = [0, 168, 169, 188, 185, 187, 161]
#p = [0, 189, 122, 161, 108, 191, 109, 173, 128]
#p = [0, 151, 182, 111, 127, 158, 156, 200, 171]
#p = [0, 171, 139, 185, 153, 168, 151, 187, 128]
#p = [0, 113, 140, 200, 184, 104, 198, 137, 110]

#p = [0, 182, 163, 124, 131, 131, 156, 136, 179]


p = [0, 124, 121, 132, 195, 145, 139]

n = len(p) - 1
data = {}
cost = 0
for i in range(3, n):
	data[(1, i)] = [(1, i-1, i), (1, i, i+1)]
	cost += p[1] * p[i-1] * p[i]

cost += p[1]*p[n-1]*p[n]
print data.keys()
print cost

while improved():
	print data.keys()
	print cost

