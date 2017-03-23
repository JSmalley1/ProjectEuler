from JTools import Factorizer

def get_abudants_below(maxim):
	vals = []

	for x in xrange(12, maxim):
		if x < sum(F.get_proper_divisors(x)):
			vals.append(x)


	return vals

F = Factorizer.Factorizer()

abundants = get_abudants_below(28124)
abunds = set(abundants)

S = 0
for v in xrange(0, 28124):
	sum_found = False
	for a1 in abundants:
		a2 = v - a1
		if a2 < a1:
			break
		if a2 in abunds:
			sum_found = True
			break
	if not sum_found:
		S += v

print S