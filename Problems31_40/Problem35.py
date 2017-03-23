from JTools import PrimeHandler as PH

def get_rotations(num):
	seen = set()
	num = str(num)
	while num not in seen:
		seen.add(num)
		num = num[1:] + num[0]
	return set(map(int, seen))

primes = set(PH.Primes(1000000).get_all_below(1000000))
count = 0
all_seen = set()

for p in primes:
	if p in all_seen:
		continue
	rots = get_rotations(p)
	all_seen |= rots

	if rots < primes:
		count += len(rots)

print count