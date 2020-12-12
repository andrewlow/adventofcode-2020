#!/usr/bin/python3
import copy

with open('input.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 

def split(word):
	return[c for c in word]

# To simplify the seating probes, we pad with floor all around
seating = []
firstLast = ['.' for c in (content[0] + '--')]
seating = seating + [firstLast]
for x in content:
	seating = seating + [split('.' + x + '.')]
seating = seating + [firstLast]

# Assume that input is well formatted and all rows are same width

def printSeating(seating):
	print('rows: ',len(seating))
	print('cols: ',len(seating[0]))
	for x in seating:
		print(x)

# return true if all surrounding spaces are not occupied
def checkEmpty(y,x):
	global seating
	if seating[x][y] == '#':
		return False
	# probe the adjacent seats
	empty = True
	if seating[x-1][y-1] == '#':
		return False
	if seating[x-1][y] == '#':
		return False
	if seating[x-1][y+1] == '#':
		return False
	if seating[x][y-1] == '#':
		return False
	if seating[x][y] == '#':
		return False
	if seating[x][y+1] == '#':
		return False
	if seating[x+1][y-1] == '#':
		return False
	if seating[x+1][y] == '#':
		return False
	if seating[x+1][y+1] == '#':
		return False
	return True

# return true if more than four surrounding seats are taken
def checkCrowded(y,x):
	global seating
	# if we get passed an empty seat, taken no action
	if seating[x][y] == 'L':
		return False 
	# probe the adjacent seats, counting occupied spaces
	count = 0
	if seating[x-1][y-1] == '#':
		count = count + 1
	if seating[x-1][y] == '#':
		count = count + 1
	if seating[x-1][y+1] == '#':
		count = count + 1
	if seating[x][y-1] == '#':
		count = count + 1
	if seating[x][y] == '#':
		count = count + 1
	if seating[x][y+1] == '#':
		count = count + 1
	if seating[x+1][y-1] == '#':
		count = count + 1
	if seating[x+1][y] == '#':
		count = count + 1
	if seating[x+1][y+1] == '#':
		count = count + 1
	return (count > 4) 
	


def fillSeats():
	global seating
	# python copy is by default a shallow one, we want a deep copy
	newSeats = copy.deepcopy(seating)

	for y in range(1,len(seating)-1):
		for x in range (1,len(seating[0])-1):
			if seating[y][x] != '.':
				if checkEmpty(x,y):
					newSeats[y][x] = '#'
	return(newSeats)

def leaveSeats():
	global seating
	newSeats = copy.deepcopy(seating)
	for y in range(1,len(seating)-1):
		for x in range (1,len(seating[0])-1):
			if seating[y][x] != '.':
				if checkCrowded(x,y):
					newSeats[y][x] = 'L'
	return(newSeats)


def countSeats():
	global seating
	count = 0
	for y in range(1,len(seating)-1):
		for x in range (1,len(seating[0])-1):
			if seating[y][x] == '#':
				count = count + 1
	return(count)
	

# printSeating(seating)
newSeats = []
done = False
while not done:
#	printSeating(seating)
	newSeats = fillSeats()
	if newSeats == seating:
		done = True
	seating = newSeats
#	printSeating(seating)
	newSeats = leaveSeats()
	if newSeats == seating:
		done = True
	seating = newSeats
	
printSeating(seating)
print('Seats occupied: ', countSeats())
