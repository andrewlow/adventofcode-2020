#!/usr/bin/python3

with open('input.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 

validRanges = []
myTicket = []
invalid = []

def rangeFromString(s):
#	print('range from string: ', s)
	chunks = s.split('-')
	a = int(chunks[0])
	b = int(chunks[1])+1 # hack range to so (1-3) says 'yes' to 3
	return(range(a,b))

i = 0
done = False
while not done:
	if content[i] == '':
		done = True
	else:
		chunks = content[i].split(':')
		chunks = chunks[1].split()
#		print(chunks)
		validRanges.append(rangeFromString(chunks[0]))
		validRanges.append(rangeFromString(chunks[2]))
#		print(validRanges)
#		print(content[i])
	i = i + 1

# read my ticket next
i = i + 1
print('ticket:', content[i])
myTicket = content[i]

# return true if valid
def isValid(n):
	global validRanges
	inRange = False
	for x in validRanges:
		if n in x:
			inRange = True
	return inRange

# Now the nearby tickets
i = i + 3 
# print('nearby: ', content[i])
done = False
while i < len(content):
#	print(content[i])
	for c in content[i].split(','):
		n = int(c)
		if not isValid(n):
#			print('Not valid: ', n)
			invalid.append(n)
	i = i + 1

# sum the invalid
sum = 0
for x in invalid:
	sum = sum + x

print('Sum: ', sum)
