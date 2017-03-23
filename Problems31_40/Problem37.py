from JTools import PrimeHandler as PH

def can_trunc_left(val):
	val /= 10

	while val:
		if val not in primes:
			return False
		val /= 10
	return True

def can_trunc_right(val):
	k = 1
	v = val % 10**k
	while v != val:
		if v not in primes:
			return False
		k += 1
		v = val % 10**k
	return True


P = PH.Primes(1000000).get_all_below(1000000)
primes = set(P)

count = 0
total = 0
for p in P:
	if p > 7 and can_trunc_right(p) and can_trunc_left(p):
		count += 1
		total += p
		if count == 11:
			break

print total
