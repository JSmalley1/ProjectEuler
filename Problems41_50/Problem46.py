from JTools import PrimeHandler as PH

def solve():
	x = 9

	primes = set(PH.Primes(1000000).get_all_below(1000000))
	index = 0
	squares = [1]

	while True:
		while squares[-1] < x:
			squares.append((len(squares)+1)**2)

		found = False
		for s in squares:
			if (x-2*s) in primes:
				found = True
				break

		if not found:
			return x

		x += 2
		while x in primes:
			x += 2

print solve()
