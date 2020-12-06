#!/usr/bin/python3

with open('input.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 

# return new array of rows
def row(choice, rows):
	if choice == 'F':
		return rows[:int(len(rows)/2)]
	elif choice == 'B':
		return rows[int(len(rows)/2):]

	else:
		print('Error')
	return

# return new arrow of col
def column(choice, col):
	if choice == 'R':
		return col[int(len(col)/2):]
	elif choice == 'L':
		return col[:int(len(col)/2)]
	else:
		print('Error')
	return

# from part1 we know the highest seat is 928 which divides into 116 rows of 8
plane = ['O']*929

# assumes ticket input is well formed
for ticket in content:
	# find row
	seats = list(range(0,128))
	for i in range(0,7):
		seats = row(ticket[i], seats)
	seatID = seats[0] * 8
	# find column
	seats = list(range(0,8))
	for i in range(7,10):
		seats = column(ticket[i], seats)
	seatID = seatID + seats[0]
	print(seatID)
	plane[seatID]='X'

i = 0
while i < 928:
	for j in range(0,8):
		print(plane[i], end='')
		i = i + 1
	print()

# search the plane for a seat that is between two taken id's
i = 1
while i < 927:
	if plane[i-1] == 'X' and plane[i] == 'O' and plane[i+1] == 'X':
		print('My Seat ID: ', i)
	i = i + 1

