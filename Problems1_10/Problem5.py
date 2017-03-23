from JTools import Factorizer as FZ
from collections import defaultdict

counts = defaultdict(int)

F = FZ.Factorizer()

for x in xrange(2, 21):
	for p, c in F.get_all_factors(x):
		counts[p] = max(counts[p], c)

total = 1
for k in counts.keys():
	total *= k ** counts[k]

print total