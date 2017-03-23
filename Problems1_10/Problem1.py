total = 0
for i in range(1000):
	if not (i % 3 and i % 5):
		total += i
print total
