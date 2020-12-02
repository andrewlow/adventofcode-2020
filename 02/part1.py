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
	min = int(v[0])
	max = int(v[1])
	# check password
	count = password.count(character)
	print('{0} count = {1}'.format( a, count))
	if count>=min and count<=max:
		valid = valid + 1

print(valid)
