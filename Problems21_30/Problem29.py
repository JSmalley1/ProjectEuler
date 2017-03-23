answer = set()

for a in xrange(2, 101):
	for b in xrange(2, 101):
		answer.add(a**b)

print len(answer)