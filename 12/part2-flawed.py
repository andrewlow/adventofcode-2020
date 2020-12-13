#!/usr/bin/python3

with open('input.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 

heading = 'E'
xway = 10
yway = 1

xpos = 0 # left right
ypos = 0 # up down

def north(n):
	global yway
	print('north')
	yway = yway + n

def south(n):
	global yway
	print('south')
	yway = yway - n

def east(n):
	global xway
	print('east')
	xway = xway + n

def west(n):
	global xway
	print('west')
	xway = xway - n

def left(n):
	global heading
	global xway
	global yway
	print('left',n)
	# assume 90's, and no more than 270
	# turning left - direction, x sign y sign
	# Rotate 90 always means swap xway/yway - sign of new values depends on direction
	#
	# I thought this was clever and correct, but got stuck
	# looking at some others talk about the solution they 
	# used 'matrix multiplication formulas for rotation of x/y coordinates'
	# seems heavy handed.
	# Other seems to have leant on existing 'vector' libraries. Hmm.
	#
	# But https://calcworkshop.com/transformations/rotation-rules/
	# confirms that my rotation approach is basically sound, and 
	# I know this by my test cases.
	#
	# By getting another solution and doing an output comparison (see cheat.py)
	# I discovered the flaw in my logic (saved as part2-flawed.py)
	# The assumption was that I could just set the sign of the xway/yway
	# based on the direction - this fails if we were heading facing north
	# but the offset was south (negative). We would discard the sign!
	#
	direction = {
		'N':['W',-1,-1],
		'E':['N',-1,1],
		'W':['S',1,-1],
		'S':['E',1,1]
	}
	for i in range(0,int(n/90)):
		d = direction[heading]
		heading = d[0]
		xtmp = xway
		xway = abs(yway) * d[1]
		yway = abs(xtmp) * d[2]

def right(n):
	global heading
	global xway
	global yway
	print('right', n)
	# assume input is good
	# turning right
	direction = {
		'N':['E',1,1],
		'E':['S',1,-1],
		'W':['N',-1,1],
		'S':['W',-1,-1]
	}
	for i in range(0,int(n/90)):
		d = direction[heading]
		heading = d[0]
		xtmp = xway
		xway = abs(yway) * d[1]
		yway = abs(xtmp) * d[2]
	

# advance by xway and yway, n times
def forward(n):
	global commands
	global xway
	global yway
	global xpos
	global ypos

	print('forward')
	for i in range(0,n):
		xpos = xpos + xway
		ypos = ypos + yway

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
	print('ROO:', xpos, ypos, xway, yway, heading)

print('X: ', abs(xpos))
print('Y: ', abs(ypos))

print('Manhattan distance: ', abs(xpos)+abs(ypos))
