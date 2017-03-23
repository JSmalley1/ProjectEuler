from JTools import PrimeHandler as PH

def solve():
	primes = PH.Primes(1000000).get_all_below(10000)
	i = 0
	while primes[i] < 1000:
		i += 1

	pset = set(primes[i:])

	found = 0
	while i < len(primes):
		p1 = primes[i]
		for j in range(i + 1, len(primes)):
			p2 = primes[j]

			if sorted(str(p1)) == sorted(str(p2)):
				dp = p2 - p1

				p3 = p2 + dp
				if p3 >= 10000:
					break

				if p3 not in pset or sorted(str(p3)) != sorted(str(p1)):
					continue
				else:
					found += 1
					print p1, p2, p3
					if found == 2:
						return
		i += 1

solve()
