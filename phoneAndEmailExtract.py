# import modules
import re
import os

# Create rules for finding phone number using regexes
phoneRule = re.compile(r'''(
    (\+ | \d{2})?
    (\s|-|\.)?
    (\d{5})
    (\s|-|\.)?
    (\d{5})
 )''', re.VERBOSE)

# Create email regex
emailRule = re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    [a-zA-Z0-9]
)''', re.VERBOSE)

# open and reading  a file and saving into text variable
text = open('text.txt').read()

# Find matches in text
matches = []
for group in phoneRule.findall(text):
    phoneNum = ''.join(group[2])
    if group[0] != '':
        phoneNum +=  (group[0])
    matches.append(phoneNum)

for group in emailRule.findall(text):
    matches.append(group)

#Displaying Results
if len(matches) > 0:
    print('Contact numbers and emails are as follow: ')
    print('\n'.join(matches))
else:
    print('No Email and contact number has been found.')
