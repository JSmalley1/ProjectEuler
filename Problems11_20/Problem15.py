def factorial(n):
	total = 1
	while n > 1:
		total *= n
		n -= 1

	return total


def choose(n, k):
	return factorial(n)/(factorial(k)*factorial(n-k))


print choose(40, 20)