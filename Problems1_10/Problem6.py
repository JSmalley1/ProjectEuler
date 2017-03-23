sos = 0
ss = 0

for i in xrange(1, 101):
	sos += i**2
	ss += i

print ss**2 - sos