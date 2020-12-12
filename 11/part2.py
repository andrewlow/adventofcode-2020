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
rmax = len(seating)-1
cmax = len(seating[0])-1
#
# Initially x, y seemed like the right coordinate system but the list is
# naturally laid out as row/column. Switching to this notation kept things 
# more sane
#

# Assume that input is well formatted and all rows are same width

def printSeating(seating):
	print('rows: ',len(seating))
	print('cols: ',len(seating[0]))
	for x in seating:
		print(x)

# Look in a given direction in the seating chart
# return True if you see someone
def look(rstart,cstart,roff,coff):
	global seating
	global cmax
	global rmax
	r = rstart
	c = cstart
#	print('look: ', r, c)
	while r > 0 and r < rmax and c > 0 and c < cmax:
		# apply offsets
		r = r + roff
		c = c + coff
#		print('probe: ', r, c, roff, coff, seating[r][c])
		if seating[r][c] == '#':
			return(True)
		# we can't see past a clear seat
		if seating[r][c] == 'L':
			return(False)
	return(False)

# return true if all surrounding spaces are not occupied
def checkEmpty(r,c):
	global seating
	if seating[r][c] == '#':
		return False
	# probe the adjacent seats
	if look(r,c, -1, -1):
		return False
	if look(r,c, 1, 1):
		return False
	if look(r,c, -1, 0):
		return False
	if look(r,c, 1, 0):
		return False
	if look(r,c, 1, -1):
		return False
	if look(r,c, -1, 1):
		return False
	if look(r,c, 0, -1):
		return False
	if look(r,c, 0, 1):
		return False
	return True

# return true if more than five surrounding seats are taken
def checkCrowded(r,c):
	global seating
	# if we get passed an empty seat, taken no action
	if seating[r][c] == 'L':
		return False 
	# probe the adjacent seats, counting occupied spaces
	count = 0
	if look(r,c, -1, -1):
		count = count + 1
	if look(r,c, 1, 1):
		count = count + 1
	if look(r,c, -1, 0):
		count = count + 1
	if look(r,c, 1, 0):
		count = count + 1
	if look(r,c, 1, -1):
		count = count + 1
	if look(r,c, -1, 1):
		count = count + 1
	if look(r,c, 0, -1):
		count = count + 1
	if look(r,c, 0, 1):
		count = count + 1
#	print('Count: ', count, r, c, count >= 5)
	return (count >= 5) 


def fillSeats():
	global seating
	# python copy is by default a shallow one, we want a deep copy
	newSeats = copy.deepcopy(seating)
	print('Fill seats')

	for r in range(1,len(seating)-1):
		for c in range (1,len(seating[0])-1):
			if seating[r][c] != '.':
				if checkEmpty(r,c):
					newSeats[r][c] = '#'
	return(newSeats)

def leaveSeats():
	global seating
	newSeats = copy.deepcopy(seating)
	print('Leave seats')
	for r in range(1,len(seating)-1):
		for c in range (1,len(seating[0])-1):
			if seating[r][c] != '.':
				if checkCrowded(r,c):
					newSeats[r][c] = 'L'
	return(newSeats)


def countSeats():
	global seating
	count = 0
	for r in range(1,len(seating)-1):
		for c in range (1,len(seating[0])-1):
			if seating[r][c] == '#':
				count = count + 1
	return(count)


# printSeating(seating)
# seating = fillSeats()
# printSeating(seating)
# seating = leaveSeats()
# printSeating(seating)
# seating = fillSeats()
# printSeating(seating)
# exit()


newSeats = []
done = False
while not done:
	printSeating(seating)
	newSeats = fillSeats()
	if newSeats == seating:
		done = True
	seating = newSeats
	printSeating(seating)
	newSeats = leaveSeats()
	if newSeats == seating:
		done = True
	seating = newSeats
	
printSeating(seating)
print('Seats occupied: ', countSeats())
