from JTools import Factorizer as FZ

tri = 3
to_add = 3

F = FZ.Factorizer()

while True:
	f = F.get_all_factors(tri)
	total = 1
	for _, count in f:
		total *= count+1

	if total > 500:
		print tri
		break

	tri += to_add
	to_add += 1