#!/usr/bin/python3

with open('input.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 

for i in range(0, len(content)):
	content[i] = int(content[i])
content.sort()
# After trying to do some brute force solutions generating all possible subsets
# the larger data sets lead to way too much memory / work
#
# We need a smart way to do this. Combinatorics will help us here
# 
# We know that all delta's are 1 or 3.
#
# For a delta of 3 - there is 1 choice
# For a delta of 1 - there may be multiple choices if we have more 1 delta's together.
#
# Ex: 456 has two 1 deltas
# choices -> 456, 46
#
# Ex: 2345 has three 1 deltas. 
# choices -> 2345, 245, 235, 25
#
# Ex: 56789 has four 1 deltas
# choices -> 56789, 5789, 5689, 5679, 579, 589, 569
#
# We have a chance of being able to find the streaks of 1's - collecting up those subsets,
# and brute forcing all combinations. This gives us a multiplier to generate the final answer

# Add the leading zero and +3 at the end
content = [0]+content+[content[len(content)-1]+3]
print(content)

def combinationsOf(list):
	# we cheat a lot - the list is always a series of values separated by 1
	# we know the longest list handed to us is 5
	answers = { 
		2:1,
		3:2,
		4:4,
		5:7}

	l = len(list)
	if l < 2 or l > 5:
		print('Error: out of range')
		exit()
	return(answers[l])

	
combinations = 1
lastValue = 0
i = 1
while i < len(content):
	delta = content[i] - lastValue
	if delta == 3:
		# There is just 1 choice, move on
		lastValue = content[i]
		i = i + 1
	elif delta == 1:
		# This is more interesting - count number of 1 delta's in a row
		j = i+1
		while j < len(content) and (content[j] - content[j-1]) == 1:
			j = j+1
		# delta between i and j is number of 1's in a row
		combinations = combinations * combinationsOf(content[i-1:j])
		lastValue = content[j-1]
		i = j
	else:
		print('Error - bad delta: ', delta)
		exit()

print('Combinations: ', combinations)
