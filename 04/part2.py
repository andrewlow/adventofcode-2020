#!/usr/bin/python3
import re

#
# Expected fields
# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)
#
# Rules
# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.
#

with open('input.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 

def validYear(yearString, min, max):
	if len(yearString) != 4:
		return False
	year = int(yearString)
	if year < min or year > max:
		return False
	return True

def validatePassport(record):
	if (('byr:' in record) and
	   ('iyr:' in record) and
	   ('eyr:' in record) and
	   ('hgt:' in record) and
	   ('hcl:' in record) and
	   ('ecl:' in record) and
	   ('pid:' in record)):
		# We know the record has all fields
		# Now we do the interesting sub-parsing to match rules
		chunks = record.split()

		for x in chunks:
			subchunks = x.split(':')
			if 'byr:' in x:
				if not validYear(subchunks[1], 1920, 2002):
					print(x)
					return False
			if 'iyr:' in x:
				if not validYear(subchunks[1], 2010, 2020):
					print(x)
					return False
			if 'eyr:' in x:
				if not validYear(subchunks[1], 2020, 2030):
					print(x)
					return False
			if 'hgt:' in x:
				unit = subchunks[1][-2:]
				height = int(subchunks[1][:-2])
				if unit == 'cm':
					if height < 150 or height > 193:
						print(x)
						return False
				elif unit == 'in':
					if height < 59 or height > 76:
						print(x)
						return False
				else:
					print(x)
					return False
			if 'hcl:' in x:
				pattern = re.compile("^#[0-9a-f]{6}$")
				if not pattern.match(subchunks[1]):
					print(x)
					return False
			if 'ecl:' in x:
				pattern = re.compile("amb|blu|brn|gry|grn|hzl|oth")
				if not pattern.match(subchunks[1]):
					print(x)
					return False
			if 'pid:' in x:
				pattern = re.compile("[0-9]{9}$")
				if not pattern.match(subchunks[1]):
					print(x)
					return False

		# If we get past all the validations, it's valid
		print('Valid: ',record)
		return True

	return False

validPassports = 0
i = 0;
while i < len(content):
	passport = ''
	while (i < len(content)) and (content[i] != ''):
		passport = passport + content[i] + ' '
		i = i + 1
	#print(passport)
	if validatePassport(passport):
		validPassports = validPassports + 1
	#print('-----')
	i = i + 1

print('Valid passports: ', validPassports)


