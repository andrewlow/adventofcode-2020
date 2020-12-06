#!/usr/bin/python3

with open('input.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 

def split(word): 
    return [char for char in word] 

i = 0;
sum = 0
while i < len(content):
	answers = []
	while (i < len(content)) and (content[i] != ''):
		answers = answers + split(content[i])
		i = i + 1
	uniq = set(answers)
	sum = sum + len(uniq)
	i = i + 1

print('Sum: ', sum)
