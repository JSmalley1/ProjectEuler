def is_palindrome(val):
	return str(val) == str(val)[::-1]

choices = set()
for x in xrange(100, 1000):
	for y in xrange(x, 1000):
		n = x * y
		if is_palindrome(n):
			choices.add(n)

print sorted(choices)[-1]