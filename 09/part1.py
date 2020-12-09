#!/usr/bin/python3

with open('input.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 


# convert to list of integers	
for i in range(0,len(content)):
	print(content[i])
	content[i] = int(content[i])

preambleLength = 5
preamble = content[0:preambleLength]

def isValid(value):
	global preamble
	for i in range(0,len(preamble)):
		for j in range(i+1, len(preamble)):
			if preamble[i] + preamble[j] == value:
				return True
	return False

for i in range(preambleLength, len(content)):
	if not isValid(content[i]):
		print('Bad value: ', content[i])
	# now rotate the preable list
	preamble.pop(0)
	preamble.append(content[i])

print('Done')
