def digit_power_sum(num):
	val = 0
	while num:
		val += (num % 10)**5
		num /= 10
	return val

total = 0
for x in xrange(2, 354294):
	if x == digit_power_sum(x):
		total += x
print total
