def is_pan_digital(val):
	string = str(val)
	return set(string) == set(map(str, range(1, len(string)+1)))

def is_prime(val):
	for y in xrange(2, 100000):
		if not val % y:
			return False
	return True

# any number using the digits 1-8 or 1-9 are divisible by 3
for x in xrange(7654321, 1, -1):
	if is_pan_digital(x) and is_prime(x):
		print x
		break

