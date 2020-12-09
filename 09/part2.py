#!/usr/bin/python3

with open('input.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 


# convert to list of integers	
for i in range(0,len(content)):
	print(content[i])
	content[i] = int(content[i])

invalidFromStep1 = 127

def sumStartingAt(index):
	global content 
	sum = content[index]
	for i in range(index+1,len(content)):
		sum = sum + content[i]
		if sum == invalidFromStep1:
			return(i)
		if sum > invalidFromStep1:
			return(-1)
	return(-1)

def smallestBetween(a, b):
	global content
	small = content[a]
	for i in range(a,b):
		if content[i] < small:
			small = content[i]
	return small

def largestBetween(a,b):
	global content
	large = content[a]
	for i in range(a,b):
		if content[i] > large:
			large = content[i]
	return large
		
for i in range(0, len(content)):
	r = sumStartingAt(i)
	if r != -1:
		s = smallestBetween(i,r)
		l = largestBetween(i,r)
		weak = s + l
		print('Weakness: ', weak)
		exit()

print('Error - not found')
