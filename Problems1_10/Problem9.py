def find_val():
	for c in range(997, 334, -1):
		for b in range(c-1, 1, -1):
			a = 1000 - b - c
			if a < 1:
				continue
			if a**2 + b**2 == c**2:
				return a * b * c

print find_val()