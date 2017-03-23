def solve():
	def factorial(n):
		while len(F) <= n:
			F.append(len(F) * F[-1])
		return F[n]

	def digit_sum(n):
		t = 0
		while n:
			t += factorial(n%10)
			n /= 10
		return t

	F = [1]

	f9 = factorial(9)
	k = 1
	while int('9'*k)<= k*f9:
		k += 1

	total = 0
	for x in xrange(3, int('9'*k)+1):
		if x == digit_sum(x):
			total += x

	return total

print solve()