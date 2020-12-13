#!/usr/bin/python3

with open('input.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 

heading = 'E'

xpos = 0 # left right
ypos = 0 # up down

def north(n):
	global ypos
	print('north')
	ypos = ypos + n

def south(n):
	global ypos
	print('south')
	ypos = ypos - n

def east(n):
	global xpos
	print('east')
	xpos = xpos + n

def west(n):
	global xpos
	print('west')
	xpos = xpos - n

def left(n):
	global heading
	print('left',n)
	# Make sure we are dealing with multiples of 90
	if n % 90 != 0:
		print('Error - unexpected angle:', n)
		exit()
	if n > 270:
		print('Error - unexpected angle:', n)
		exit()
	# turning left
	direction = {
		'N':'W',
		'E':'N',
		'W':'S',
		'S':'E'
	}
	for i in range(0,int(n/90)):
		heading = direction[heading]
	print('New heading: ', heading)
	

def right(n):
	global heading
	print('right', n)
	# Make sure we are dealing with multiples of 90
	if n % 90 != 0:
		print('Error - unexpected angle:', n)
		exit()
	if n > 270:
		print('Error - unexpected angle:', n)
		exit()
	# turning right
	direction = {
		'N':'E',
		'E':'S',
		'W':'N',
		'S':'W'
	}
	for i in range(0,int(n/90)):
		heading = direction[heading]
	print('New heading: ', heading)
	

def forward(n):
	global commands
	global heading
	print('forward')
	commands[heading](n)

commands = {
	'N':north,
	'S':south,
	'E':east,
	'W':west,
	'L':left,
	'R':right,
	'F':forward
}

for x in content:
	print(x)
	code = x[0]
	value = int(x[1:])
	commands[code](value)

print('X: ', abs(xpos))
print('Y: ', abs(ypos))

print('Manhattan distance: ', abs(xpos)+abs(ypos))
