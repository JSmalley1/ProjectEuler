def solve():
	def is_hex(num):
		return ((1+8*num)**0.5) % 4 == 3

	T = 3
	Tadd = 3
	P = 5
	Padd = 7

	while True:
		if T == P and is_hex(T):
			if T > 40755:
				return T
			T += Tadd
			Tadd += 1

		elif T < P:
			T += Tadd
			Tadd += 1
		else:
			P += Padd
			Padd += 3

print solve()
