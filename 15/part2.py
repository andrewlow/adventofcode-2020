#!/usr/bin/python3

input = [0,3,6]
#input = [1,3,2]
#input = [2,1,3]
#input = [1,2,3]
#input = [3,2,1]
#input = [3,1,2]

# keeping the whole list like in part1 doesn't scale
# using a pair of dictionaries

# start with last [0,3,6]
# last number is 6, does not appear in before because it is only in last
# add a new number 0 - no need to cascade to before because it's new
# last number is 0, does appear in before.
# calculate 3 - appears in last, so copy to before, add to last
#
before = {}
last = {}
count = len(input)+1
lastValue = input[len(input)-1]

end = 30000000
#end = 2020

# populate the last dictionary
for i in range(0,len(input)):
	last[input[i]] = i+1

#fakeinput = ['x'] + input

while count != end + 1:
#	print(fakeinput, before, last)
#	print(fakeinput)
	if count % 1000000 == 0:
		print(count)
	# have we seen the last value before?
	if lastValue not in before:
		# add zero
		if 0 in last:
			# cascade to before
			before[0] = last[0]
		last[0] = count
		lastValue = 0
	else:
		# Yes calculate the new value
#		print(last[lastValue])
#		print(before[lastValue])
		new = last[lastValue] - before[lastValue]
		# if this is a duplicate, update last
		if new in last:
			# cascade to before
			before[new] = last[new]
		# add to last
		last[new] = count
		lastValue = new
#	fakeinput = fakeinput + [lastValue]
	count = count + 1
		
print('Last:', lastValue)
