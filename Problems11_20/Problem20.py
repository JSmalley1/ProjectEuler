def factorial(n):
	total = 1
	while n > 1:
		total *= n
		n -= 1
	return total

s = 0
val = factorial(100)
while val:
	s += val%10
	val /= 10

print s