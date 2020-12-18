#!/usr/bin/python3

with open('input.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 


# Locate the first (a+b) expression range
def subExpression(s):
	e = s.find(')')
	if e == -1:
		return('')
	b = s.rfind('(', 0, e)
	return(s[b:e+1])

def doMath(a, op, b):
	if op == '+':
		return int(a) + int(b)
	elif op == '*':
		return int(a) * int(b)
	else:
		print('Error', a, op, b)
		exit()

def solveExpression(s):
	c = s.split()
#	print(c)
	if len(c) == 3:
		return(doMath(c[0], c[1], c[2]))
	# more than 1 expression - do addition first
	while c.count('+') != 0:
		i = c.index('+')
		a = doMath(c[i-1], c[i], c[i+1])
		del c[i:i+2]
		c[i-1] = a
#		print(c)

	# Now do all of the *'s
	sum = int(c[0])
	i = 1 
	while i < len(c):
		op = c[i]
		v = int(c[i+1])
		sum = doMath(sum, op, v)
		i = i + 2
		
	return(sum)

total = 0
for x in content:
	eq = x
	sub = subExpression(eq)
	while sub != '':
#		print(sub)
		# there is a sub expression, go solve it
		s = sub[1:len(sub)-1]
		a = solveExpression(s)
		# compose a new expression by removing the sub-expression
		b = eq.find(sub)
		eq = (eq[:b]) + str(a) + (eq[b+len(sub):])
#		print(eq)
		sub = subExpression(eq)
	a = solveExpression(eq)
	print(x, ' becomes', a)
	total = total + a

print('Sum: ', total)
