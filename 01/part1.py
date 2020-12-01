#!/usr/bin/python3

with open('input.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 

for x in content:
	for y in content:
		sum = int(x) + int(y)
		if sum == 2020:
			prod = int(x) * int(y)
			print('%d * %d = %d', x, y, prod)

