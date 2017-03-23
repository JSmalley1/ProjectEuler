total = 1
dx = 2
val = 1

for _ in xrange(1001 / 2):
	for n in range(4):
		val += dx
		total += val
	dx += 2

print total