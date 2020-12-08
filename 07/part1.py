#!/usr/bin/python3

# Uses the pip module 'parse'
from parse import *

with open('input.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 


# Rules are in the format
#
# <color> bags contain <number> <color> bag, <number> <color> bags.
#
	

def parseRule(rule):
#	print(rule)
	x = rule.partition('bags contain')
	key = x[0].strip()
#	print('Key: ',[key])
	remain = rule[len(x[0])+len(x[1]):]
	values = []
	for r in remain.rstrip('.').split(','):
		parsed = False
#		print('r:', r)
		x = parse("{:d} {} bags", r)
		if(x):
			parsed = True
			values = values + [[x[0], x[1]]]
		x = parse("{:d} {} bag", r)
		if(x):
			parsed = True
			values = values + [[x[0], x[1]]]
		if(r == " no other bags"):
			parsed = True
			values = values + []
		if not parsed:
			print("Error")
			print(r)
			print("Error")
			exit()
#	print("Values")
#	print(values)
#	print("------")
	return([key, values])

rules = {}
for x in content:
	r = parseRule(x)
	print('RULE:', r)
	rules[r[0]] = r[1]

#print(rules)

# Now we have the rules, we answer the question how many bags could contain a shiny gold bag

def containsBag(color):
	bagTypes = []
	for x in rules:
		if rules[x] != None:
			for y in rules[x]:
				if y[1] == color:
					bagTypes.append(x)
					bagTypes = bagTypes + containsBag(x)
#	print('Color: ', color)
#	print('Contained in: ', bagTypes)
	return(bagTypes)


allBags = containsBag('shiny gold')
count = len(set(allBags))

print(allBags)
print('Count: ',count)

	
