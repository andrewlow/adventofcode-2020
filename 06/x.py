#!/usr/bin/python3

with open('input.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 

def split(word): 
    return [char for char in word] 

sum = 0
i = 0;
while i < len(content):
	answers = []
	while (i < len(content)) and (content[i] != ''):
		answers.append(split(content[i]))
		i = i + 1
	overlap = answers[0]
	for e in range(1, len(answers)):
		overlap = list(set(overlap) & set(answers[e]))
	sum = sum + len(overlap)
	print('Content: ', answers)
	print('Overlap: ', overlap, len(overlap))
	i = i + 1
print ('Sum: ', sum)
