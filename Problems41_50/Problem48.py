answer = 0
mod = 10000000000

for x in xrange(1,1001):
	answer = (answer + (x**x) % mod)% mod

print answer