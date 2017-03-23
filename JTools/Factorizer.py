import PrimeHandler


class Factorizer(object):
	def __init__(self):
		self.alive = True

	def get_all_factors(self, num):
		if num <= 1:
			return []

		factors = []
		twos = 0
		while not num % 2:
			twos += 1
			num /= 2

		if twos:
			factors.append((2, twos))

		x = 3
		while num > 1:
			total = 0
			while not num % x:
				total += 1
				num /= x
			if total:
				factors.append((x, total))
			x += 2
		return factors

	def get_proper_divisors(self, num):
		factors = [1]

		for x in xrange(2, num/2 + 1):
			if not num % x:
				factors.append(x)

		return factors

	def get_divisors(self, num):
		return self.get_proper_divisors(num) + [num]