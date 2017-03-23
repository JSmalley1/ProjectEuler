coins = [1, 2, 5, 10, 20, 50, 100, 200]

D = dict()
D[0] = set()
D[1] = set()
D[1].add((1,))

for x in xrange(2, 201):
	this = set()
	for coin in coins:
		if coin <= x:
			for tup in D[x-coin]:
				this.add(tuple(sorted(tup + (coin,))))
		if x == coin:
			this.add((coin, ))
	D[x] = this

print len(D[200])
