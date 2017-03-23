from JTools import PrimeHandler

num = 600851475143
val = int(num**0.5)

P = PrimeHandler.Primes(val)

left = 0
right = len(P.primes)-1

while left + 1 < right:
	mid = int((right+left)/2)
	if P.primes[mid] <= val:
		left = mid
	else:
		right = mid

while right >= 0:
	if not num % P.primes[right]:
		print P.primes[right]
		break
	right -= 1
