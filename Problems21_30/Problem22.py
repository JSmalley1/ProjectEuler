def name_score(string):
	return sum(map(lambda x: ord(x)-ord('a')+1, string))

names = []

with open('p022_names.txt', 'r') as f:
	for line in f:
		line = line.strip().split(',')
		for n in line:
			names.append(n.lower()[1:-1])

names = sorted(names)

score = 0
for i in range(len(names)):
	score += (i+1) * name_score(names[i])
print score