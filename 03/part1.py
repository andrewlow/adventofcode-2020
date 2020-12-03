#!/usr/bin/python3

with open('input.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 

# tragectory
right = 3
down = 1

lines = 0
length = len(content[0])
for x in content:
	lines = lines + 1
	if len(x) != length:
		print('Line length variation')

depth = int(lines / down)
width = int(right * depth)
print('Depth: ', depth )
print('Width: ', width )
slope = []

for i in range(lines):
	slope.append('')

i = 0
for x in content:
	while len(slope[i]) < width:
		slope[i] = slope[i] + x
	i  = i + 1

print()
for x in slope:
	print(x)

# Now we go down the slope

position = 0
tree = 0
i = 0
while i < lines:
	# check for a tree at position
	if slope[i][position] == '#':
		slope[i] = slope[i][:position] + 'X' + slope[i][position + 1:]
		tree = tree + 1
	else:
		slope[i] = slope[i][:position] + 'O' + slope[i][position + 1:]
	position = position + right
	i = i + down

print()
for x in slope:
        print(x)

print('Tree count: ', tree)
