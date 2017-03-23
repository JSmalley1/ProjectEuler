def solve():
	def evaluate(val):
		if val in seen:
			return D[val]
		seen.add(val)
		D[val] = 1 + evaluate(3*val+1 if val % 2 else val/2)
		return D[val]

	D = dict()
	D[1] = 1
	seen = set()
	seen.add(1)

	m = 0
	start = 0

	for x in xrange(2, 1000000):
		length = evaluate(x)
		if length > m:
			m = length
			start = x

	return start

print solve()