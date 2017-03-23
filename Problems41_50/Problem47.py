def solve():
	facts = [set(), set(), {2}, {3}]

	while True:
		if all(map(lambda x: len(x) == 4, facts[-4:])):
			return len(facts) - 4

		this_set = set()
		val = len(facts)

		i = 2
		while i <= val:
			if val % i == 0:
				this_set.add(i)
				val /= i
				this_set |= facts[val]
				break
			i += 1
		facts.append(this_set)

print solve()
