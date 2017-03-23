def fact(n):
	total = 1
	while n > 1:
		total *= n
		n -= 1

	return total

ret = ''
vals = map(str, range(10))

perm = 999999

while perm:
	temp = fact(len(vals)-1)
	index = perm / temp
	perm -= temp*index
	ret += vals[index]
	vals = vals[:index] + vals[index+1:]

ret += ''.join(vals)

print ret