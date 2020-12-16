#!/usr/bin/python3

with open('input.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 

mask = ''
ones = ''
zeros =  ''
omask = 0
zmask = 0
memory = {}
for x in content:
	chunks = x.split()
	if chunks[0] == 'mask':
		mask = chunks[2]
		ones = mask.replace('X','1')
		zeros = mask.replace('X', '0')
		print(mask)
		print(ones, int(ones,2))
		print(zeros, int(zeros,2))
		omask = int(ones,2)
		zmask = int(zeros,2)
	if chunks[0][:3] == 'mem':
		n = int(x.split(']')[0].split('[')[1])
		print(n)
		v = int(chunks[2])
		d = (v & omask)| zmask
		print(d)
		memory[n] = d

print('memory: ', memory)
sum = 0
for x in memory:
	sum = sum + memory[x]

print('Sum: ', sum)
