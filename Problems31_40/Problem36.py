def is_ten_pal(val):
	if not val%10:
		return False
	return str(val) == str(val)[::-1]

def is_two_pal(val):
	val = bin(val)[2:]
	if val[-1] == '0':
		return False

	return val == val[::-1]

total = 0
for x in xrange(1, 1000000):
	if is_ten_pal(x) and is_two_pal(x):
		total += x

print total