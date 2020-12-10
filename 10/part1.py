#!/usr/bin/python3

with open('input.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 

for i in range(0, len(content)):
	content[i] = int(content[i])
content.sort()
print(content)
delta1 = 0
delta3 = 1

lastValue = 0

for i in range(0,len(content)):
	delta = content[i] - lastValue
	if delta == 1:
		delta1 = delta1 + 1
	elif delta == 3:
		delta3 = delta3 + 1
	else:
		print('Error - bad delta: ', delta)
		exit()
	lastValue = content[i]

print('Delta 1: ', delta1)
print('Delta 3: ', delta3)
print('Product: ', delta1 * delta3)
