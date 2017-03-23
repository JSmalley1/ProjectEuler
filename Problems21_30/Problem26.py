def find_recurring(denom):
	seen = set()
	lengths = dict()

	rem = 1
	answer = ''

	while rem and rem not in seen:
		seen.add(rem)
		lengths[rem] = len(answer)
		val = rem*10
		answer += str(val / denom)

		rem = val % denom

	if rem == 0:
		return -1
	return answer[lengths[rem]:]

longest = 0
denominator = -1
for i in xrange(2, 1001):
	pattern = find_recurring(i)
	if pattern != -1 and len(pattern) > longest:
		longest = len(pattern)
		denominator = i

print denominator