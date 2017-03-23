from JTools import PrimeHandler as PH

P = PH.Primes(1000000)

primes = set(P.primes)

most = 0
prod = 0

for a in xrange(-999, 1000):
	for b in range(-1000, 1001):
		n = 0
		while n**2 + a*n + b in primes:
			n += 1
		if n > most:
			most = n
			prod = a * b

print prod