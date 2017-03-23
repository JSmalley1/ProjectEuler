total = 0
last = 1
current = 2

while current < 4000000:
	if not current % 2:
		total += current
	last, current = current, last + current

print total
