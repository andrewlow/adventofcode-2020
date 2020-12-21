#!/usr/bin/python3

with open('input.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 

def ingredients(s):
	c = s.split()
	return c

def allergens(s):
	c = s.strip(')').split(',')
	f = c[0].split()
	c[0] = f[1]
	for i in range(len(c)):
		c[i] = c[i].strip()
	return c

all = []
	
for x in content:
	c = x.split('(')
	i = ingredients(c[0])
	a = allergens(c[1])
	all.append([set(i),set(a)])

def findOne():
	global all
	singles = {}
	for i in range(len(all)):
		for j in range(i+1,len(all)):
			m = all[i][0].intersection(all[j][0])
			n = all[i][1].intersection(all[j][1])
			if len(m) == 1 and len(n) == 1:
				# we have found one ingredient that matches
				return [m.pop(), n.pop()]
			if len(n) == 1:
				k = n.pop()
				if k in singles:
					# merge to make new intersection
					singles[k] = singles[k].intersection(m)
				else:
					# just add it
					singles[k]= m
	# if we get here, we have a list of singles that should cook down, or we are really done
	for x in singles:
		if len(singles[x]) == 1:
			return[singles[x].pop(), x]
	return []

#
result = { }
none = []
#
match = findOne() 
while len(match) != 0:
	i = match[0]
	a = match[1]
	result[a] = i

	# now modify all to remove the match
	for x in range(len(all)):
		e = all[x]
		if i in e[0]:
			e[0].remove(i)
		if a in e[1]:
			e[1].remove(a)
		if len(e[1]) == 0:
			# no more allergens, all ingredients are cleaqn
			none = none + list(e[0])
			e[0]=set()
				
	
	match = findOne()	

for x in all:                           
	if len(x[1])==1 and len(x[0])==1:
		result[x[1].pop()] = x[0].pop()
	if len(x[1])==0:
		none = none + list(x[0])

print('All: ',all)
print('Result: ',result)
print('None: ',none)

z = list(result.keys())
z.sort()
answer = ''
for y in z:
	answer = answer + result[y] + ','

print('Answer: ', answer)
