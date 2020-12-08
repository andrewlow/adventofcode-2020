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

# Now we have the rules, we answer the question how many bags can shiny gold bag contain

def inBag(color):
	bags = 0
	for b in rules:
		if b == color:
			print(b)
			print(rules[b])
			# base case - empty bag, just count this bag
			if len(rules[b]) == 0:
				return(0)
			# for every bag, count how many we have
			for c in rules[b]:
				subBags = inBag(c[1])
				bagCount = c[0]
				print(bagCount, subBags)
				bags = bags + (bagCount * subBags) + bagCount
	return(bags)

count = inBag('shiny gold')
print('Count: ',count)

	
