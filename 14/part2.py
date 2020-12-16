#!/usr/bin/python3

with open('input.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 

# Return a list of all numbers by swapping X's
def allNumbers(s):
	if 'X' not in s:
		return [int(s,2)]
	i = s.index('X')
	s1 = s[:i]+'0'+s[i+1:]
	s2 = s[:i]+'1'+s[i+1:]
#	print(s1,s2)
	return(allNumbers(s1) + allNumbers(s2))

def maskAddr(s,n):
	m = "0000000000000000000000000000000000000000{0:b}".format(n)
	m = m[-36:]
#	print('maskAddr', s, m)
	l = []
	for i in range(len(s)):
		if s[i] == 'X':
			l.append('X')
		elif s[i] == '1':
			l.append('1')
		else:
			l.append(m[i])
	s = "".join(l)
#	print('new mask', s)
	return(s)
	

mask = ''
memory = {}
for x in content:
	chunks = x.split()
	if chunks[0] == 'mask':
		mask = chunks[2]
	if chunks[0][:3] == 'mem':
		n = int(x.split(']')[0].split('[')[1])
#		print('address',n)
#		print('mask',mask)
		na = maskAddr(mask,n)
		l = allNumbers(na)
		v = int(chunks[2])
#		print('value',v)
		for a in l:
			memory[a] = v

print('memory: ', memory)
sum = 0
for x in memory:
	sum = sum + memory[x]

print('Sum: ', sum)
