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

highestSeat = 0
# assumes ticket input is well formed
for ticket in content:
	# find row
	seats = list(range(0,128))
	for i in range(0,7):
		seats = row(ticket[i], seats)
	print('Seat: ', seats[0])
	seatID = seats[0] * 8
	# find column
	seats = list(range(0,8))
	for i in range(7,10):
		seats = column(ticket[i], seats)
	print('Column: ', seats[0])
	seatID = seatID + seats[0]
	print('seat ID: ', seatID)
	if seatID > highestSeat:
		highestSeat = seatID

print('Highest seat id: ', highestSeat)
