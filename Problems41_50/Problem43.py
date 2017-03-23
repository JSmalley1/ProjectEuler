from itertools import permutations
from collections import defaultdict


def get_pan_digit(string):
	s_set = set(string)
	if len(string) != len(s_set):
		return 0
	missing = set('0123456789') - s_set
	return int(missing.pop())*1000000000 + int(string)

D = defaultdict(set)

divisors = [2, 3, 5, 7, 11, 13, 17]
total = 0
for p in permutations('0123456789', 3):
	val = int(''.join(p))
	for d in divisors:
		if not val % d:
			D[d].add(''.join(p))

seen = set()
for seventeen in D[17]:
	for thirteen in D[13]:
		if thirteen[1:] == seventeen[:2]:

			for eleven in D[11]:
				if eleven[1:] == thirteen[:2]:

					for seven in D[7]:
						if seven[1:] == eleven[:2]:

							for five in D[5]:
								if five[1:] == seven[:2]:

									for three in D[3]:
										if three[1:] == five[:2]:

											for two in D[2]:
												if two[1:] == three[:2]:
													seen.add(two[0]+three[0]+five[0]+seven[0]+eleven[0]+thirteen[0]+seventeen)

for val in seen:
	total += get_pan_digit(val)

print total