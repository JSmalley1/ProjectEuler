digits = [0, 9, 99, 999, 9999, 99999, 999999]

x = 1
index = 0

total = 1

while digits:
	val = str(x)
	if digits[0] < index + len(val):
		total *= int(val[digits[0]-index])
		digits = digits[1:]
	index += len(val)
	x += 1
	val = str(x)

print total