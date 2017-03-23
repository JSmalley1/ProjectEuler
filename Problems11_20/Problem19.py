import datetime

# Using built-in functions because why wouldn't you?
total = 0

for year in xrange(1901, 2001):
	for month in xrange(1, 13):
		if datetime.date(year, month, 1).isoweekday() == 7:
			total += 1

print total