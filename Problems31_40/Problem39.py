max_size = 0
max_p = 0

for p in xrange(1, 1001):
	num = 0
	for a in range(1, p):
		for b in range(a, (p-a)/2):
			c = p - a - b

			if c <= b:
				continue

			if a**2 + b**2 == c**2:
				num += 1
	if num > max_size:
		max_size = num
		max_p = p

print max_p