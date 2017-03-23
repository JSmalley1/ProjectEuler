def solve():
	pents = set()
	i = 1

	while True:
		P = i*(3*i-1)/2

		for val in pents:
			if P-val in pents and P-2*val in pents:
				return P-2*val
		pents.add(P)
		i += 1

print solve()