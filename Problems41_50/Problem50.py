from JTools import PrimeHandler as PH

def solve():
	limit = 1000000
	vals = PH.Primes().get_all_below(limit)
	p_set = set(vals)
	base = vals

	maxim = vals[-1]
	height = 1

	while True:
		row = []
		this_max = 0
		for i in range(len(vals)-1):
			s = vals[i] + base[height + i]

			if s >= limit:
				break
			if s in p_set:
				this_max = max(this_max, s)
			row.append(s)

		if this_max:
			maxim = this_max

		if not row:
			return maxim

		vals = row
		height += 1

print solve()
