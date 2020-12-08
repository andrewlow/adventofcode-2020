#!/usr/bin/python3

with open('input.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 

program = ()
for x in content:
	line = x.split()
	element = (line[0], int(line[1]))
	program = program + (element,)

# The program is now in a tuple of tuples

# CPU state
pc = 0
accumulator = 0

# Declare the ops
def acc(offset):
	global accumulator
	print('acc', offset)
	accumulator = accumulator + offset

def jmp(offset):
	global pc
	print('jmp', offset)
	# deal with the fact the PC already move forward
	pc = pc + offset - 1

def nop(offset):
	print('nop', offset)

ops = { 'acc':acc,
	'jmp':jmp,
	'nop':nop
	}

def runProgram(code):
	global pc
	global accumulator
	pc = 0
	accumulator = 0
	seen = set()
	while (pc not in seen) and (pc != len(code)):
		seen.add(pc)
		op = code[pc][0]
		arg = code[pc][1]
		pc = pc + 1
		ops[op](arg)

def printProgram(code):
	print("--------")
	for x in code:
		print(x)

#
for i in range(0,len(program)):
	copy = list(program)
	if copy[i][0] == 'jmp':
		copy[i] = ('nop', 0)
		printProgram(tuple(copy))
		runProgram(tuple(copy))
		if pc == len(program):
			print('Accumulator: ', accumulator)
			exit()
	


