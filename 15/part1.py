#!/usr/bin/python3

# pad the front of input to avoid python 0 based index
input = ['x', 0,3,6]
#input = ['x', 1,3,2]
#input = ['x', 2,1,3]
#input = ['x', 1,2,3]
#input = ['x', 3,2,1]
#input = ['x', 3,1,2]


end = 2020

cur = len(input)

def findLastStartingAt(l,e,b):
	for i in range(b,0,-1):
		if e == l[i]:
			return i
	return -1


while len(input) != (end +1):
#	print(input)
	# grab the last number
	last = input[len(input)-1]
	f = findLastStartingAt(input,last,len(input)-2)
#	print('found: ', last,f)
	if f == -1:
		# not in list, add zero
		input = input + [0]
	else:
		# was in list
		input = input + [(len(input)-1) - f]
print(input)
print('Last: ', input[len(input)-1])
		
