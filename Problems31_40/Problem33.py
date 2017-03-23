def reduce_fraction(num, denom):
	for x in xrange(2, num+1):
		while not (num % x) and not (denom % x):
			num /= x
			denom /= x
	return num, denom

def bad_reductions(num, denom):
	reds = set()

	a1, a2 = divmod(num, 10)
	b1, b2 = divmod(denom, 10)

	if a1 == b1 and a2 < b2:
		reds.add(reduce_fraction(a2, b2))
	if a1 == b2 and a2 < b1:
		reds.add(reduce_fraction(a2, b1))
	if a2 == b1 and a1 < b2:
		reds.add(reduce_fraction(a1, b2))
	if a2 == b2 and a2 and a1 < b1:
		reds.add(reduce_fraction(a1, b1))

	return reds

fracs = set()
for denominator in xrange(11, 100):
	for numerator in xrange(11, denominator):
		n, d = reduce_fraction(numerator, denominator)
		if (n, d) in bad_reductions(numerator, denominator):
			fracs.add((n,d))

top = 1
bottom = 1
for f1, f2 in fracs:
	top *= f1
	bottom *= f2

print reduce_fraction(top, bottom)[1]