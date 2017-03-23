import math
from os import path


class Primes(object):
	def __init__(self, limit=1000000):
		self.primes = []
		self.size = 0

		self.read_primes()
		if self.size >= limit:
			return

		top = 1000000
		diff = 1000000
		while top < self.size:
			top += diff
		while top < limit:
			self.generate_primes(max(top-diff, self.size), top)
			top += diff
		self.generate_primes(max(top-diff, self.size), limit)

		self.write_primes(limit)

	def generate_primes(self, start, end):
		print "Generating primes between {0} and {1}".format(start, end)
		num = end-start
		if not num:
			return
		sieve = [False]*(num+1)
		for x in xrange(1, int(math.sqrt(end))+1):
			temp = start-3*x**2
			for y in xrange(max(1, int((start-3*x**2)**0.5) if temp > 0 else 1), int(math.sqrt(end))+1):
				n = 4*x**2 + y**2
				if start <= n <= end and (n % 12 in (1, 5)):
					sieve[n-start] = not sieve[n-start]
				n = 3*x**2 + y**2
				if start <= n <= end and n % 12 == 7:
					sieve[n-start] = not sieve[n-start]
				n = 3*x**2 - y**2
				if x > y and start <= n <= end and n % 12 == 11:
					sieve[n-start] = not sieve[n-start]

		if start == 0:
			for x in xrange(5, int(math.sqrt(end))):
				if sieve[x]:
					for y in xrange(x**2, end+1, x**2):
						sieve[y] = False
			for p in xrange(5, end+1):
				if sieve[p]:
					self.primes.append(p)
		else:
			for p in self.primes:
				if p > int(end**0.5):
					break
				val = p**2
				while val < start:
					val += p**2
				while val <= end:
					sieve[val-start] = False
					val += p**2
			for i in xrange(len(sieve)):
				if sieve[i]:
					y = (start+i)**2
					while y <= end:
						sieve[y - start] = False
						y += (start+i)**2
					# for y in xrange((start+i)**2, end+1, (start+i)**2):
					# 	sieve[y-start] = False

					self.primes.append(i+start)

	def write_primes(self, maxim):
		with open('prime_data.txt', 'w') as f:
			f.write('{0}\n'.format(maxim))

			f.write(' '.join(map(str, self.primes)))

	def read_primes(self):
		if path.exists('prime_data.txt'):
			with open('prime_data.txt', 'r') as f:
				size = 0
				for line in f:
					line = line.strip()
					if not size:
						size = int(line)
					else:
						self.primes = map(int, line.split(' '))
				self.size = size
		else:
			self.primes = [2, 3]

	def get_all_below(self, maxim):
		left = 0
		right = len(self.primes) - 1
		mid = int((left+right)/2)

		while mid not in (left, right):
			if self.primes[mid] <= maxim:
				left = mid
			else:
				right = mid
			mid = int((left+right) / 2)

		if self.primes[right] > maxim:
			return self.primes[:right]
		return self.primes[:right+1]