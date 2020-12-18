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


def solveExpression(s):
	c = s.split()
	if c[1] == '+':
		sum = int(c[0]) + int(c[2])
	elif c[1] == '*':
		sum = int(c[0]) * int(c[2])
	else:
		print('Error', c)
		exit()	
	i = 3
	while i < len(c):
		op = c[i]
		v = int(c[i+1])
		if op == '+':
			sum = sum + v
		elif op == '*':
			sum = sum * v
		else:
			print('Error', op, v)
			exit()
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
