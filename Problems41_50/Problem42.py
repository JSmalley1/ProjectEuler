def solve():
	def is_triangular(val):
		while val > T[-1]:
			T.append(T[-1]+len(T)+1)
		return val in T

	def convert_to_int(word):
		total = 0
		for char in word:
			total += ord(char) - ord('A') + 1
		return total

	T = [1]

	num = 0
	with open('p042_words.txt', 'r') as f:
		for line in f:
			line = line.strip()
			line = line.split(',')

			for w in line:
				if is_triangular(convert_to_int(w[1:-1])):
					num += 1

	return num

print solve()