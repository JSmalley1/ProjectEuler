# def is_pan_digit(first, second, third):
# 	return set(str(first)) | set(str(second)) | set(str(third)) == set('123456789')
seen = set()
total = 0
for first in xrange(2, 100):
	second_start = 123 if first > 9 else 1234
	second_end = 10000 / first + 1
	for second in xrange(second_start, second_end):
		third = first * second

		val = str(first) + str(second) + str(third)
		if len(val) == 9 and set(val) == set('123456789'):
			if third not in seen:
				total += third
				seen.add(third)

print total