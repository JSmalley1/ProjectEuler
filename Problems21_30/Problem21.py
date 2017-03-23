from JTools import Factorizer as FZ

def sum_of_divisors(num):
	return sum(F.get_proper_divisors(num))

seen = set()
pairs = set()
F = FZ.Factorizer()

for x in xrange(1, 10000):
	if x in seen:
		continue
	seen.add(x)
	y = sum_of_divisors(x)
	if y in seen:
		continue
	seen.add(y)
	if x == sum_of_divisors(y):
		pairs.add(x)
		pairs.add(y)
		
print sum(pairs)
