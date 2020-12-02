#!/usr/bin/python3

with open('input.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 

valid = 0
for x in content:
	# parse the input line
	a = x.split()
	range = a[0]
	character = a[1][0]
	password = a[2]
	# bust apart the range into two values
	v = range.split('-')
	one = int(v[0])
	two = int(v[1])
	# check password
	first = password[one-1] == character
	second = password[two-1] == character
	print('{0} first {1} second {2}'.format( a, first, second))
	if (first and not second) or (not first and second):
		valid = valid + 1

print(valid)
