ones = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4]
teens = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
tens = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6]

# initialize with the length of "one thousand"
total = len('onethousand')

for x in xrange(1, 1000):
	h = x / 100
	if h:
		total += len('hundred') + (len('and') if x%100 else 0) + ones[h]
	two_digit = x % 100
	if two_digit < 10:
		total += ones[two_digit]
	elif two_digit < 20:
		total += teens[two_digit % 10]
	else:
		total += tens[two_digit/10] + ones[two_digit%10]

print total