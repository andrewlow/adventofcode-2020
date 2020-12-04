#!/usr/bin/python3

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

with open('input.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 


def validatePassport(record):
	if (('byr:' in record) and
	    ('iyr:' in record) and
	    ('eyr:' in record) and
	    ('hgt:' in record) and
	    ('hcl:' in record) and
	    ('ecl:' in record) and
	    ('pid:' in record)):
		return True
	return False

validPassports = 0
i = 0;
while i < len(content):
	passport = ''
	while (i < len(content)) and (content[i] != ''):
		passport = passport + content[i]
		i = i + 1
	#print(passport)
	if validatePassport(passport):
		validPassports = validPassports + 1
	#print('-----')
	i = i + 1

print('Valid passports: ', validPassports)


