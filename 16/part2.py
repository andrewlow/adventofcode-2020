#!/usr/bin/python3

with open('input.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 

validRanges = []
myTicket = []
category = {}
validTickets = []

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
		name = chunks[0]
		chunks = chunks[1].split()
#		print(chunks)
		r1 = rangeFromString(chunks[0])
		r2 = rangeFromString(chunks[2])
		validRanges.append(r1)
		validRanges.append(r2)
		category[name] = [r1,r2]
#		print(validRanges)
#		print(content[i])
	i = i + 1

print(category)
# read my ticket next
i = i + 1
print('ticket:', content[i])
mt = content[i].split(',')
for x in mt:
	myTicket.append(int(x))

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
	goodTicket = True
	ticket = []
	for c in content[i].split(','):
		n = int(c)
		ticket.append(n)
		if not isValid(n):
#			print('Not valid: ', n)
			goodTicket = False
	if goodTicket:
		validTickets.append(ticket)
	i = i + 1

print('Good Tickets: ', validTickets)

# modify dictionary to eliminate entries which don't match n
def trimSet(d,n):
	k = list(d.keys())
	for e in k:
		if not ((n in d[e][0]) or (n in d[e][1])):
			del d[e]

# for every entry in a ticket, create a unique dictionary of catgories
allTix = []
for i in range(0,len(validTickets[0])):
	allTix.append(category.copy())

# now we walk through each of the valid tickets and trim down the allTix dictionaries
for i in range(len(validTickets)):
	for j in range(len(validTickets[0])):
		d = allTix[j]
		v = validTickets[i][j]
		trimSet(d,v)

# allTix might contain multiple categories for each field, but at least 1 will be a singleton
# We need to iterate over allTix to remove the singleton duplicates from other fields

# return True if allTix is only singletons
def allTixUnique():
	global allTix
	for x in allTix:
		if len(x) > 1:
			return False
	return True

print(allTixUnique())

def trimAll(i):
	k = (list(allTix[i].keys())[0])	
	for j in range(len(allTix)):
		if j != i:
			d = allTix[j]
			if k in d:
				del d[k]
			

while not allTixUnique():
	print('try')
	# iterate looking for the any single entry
	for i in range(len(allTix)):
		e = allTix[i]
		if len(e) == 1:
			trimAll(i)

# now all tix is the map of the index of the field type
print(allTix)

# multiply all fields in myTicket that start with departure
sum = 1
for i in range(len(allTix)):
	k = list(allTix[i].keys())[0]
	print('key',k)
	if k.split()[0] == 'departure':
		print(k, myTicket[i])
		sum = sum * myTicket[i]

print('Product: ', sum)
