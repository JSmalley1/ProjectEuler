def is_pandigital(val):
	return set(val) == set('123456789')

m = 0
for x in xrange(9000, 10000):
	n = 1
	string = str(x)
	string_set = set(string)

	while len(string) < 9 and len(string) == len(string_set):
		n += 1
		string += str(n * x)
		string_set |= set(str(n*x))
	if n > 1 and len(string) == 9 and is_pandigital(string):
		m = max(m, int(string))

print m