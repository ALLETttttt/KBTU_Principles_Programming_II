import re

word = input()

pattern = '^[A-Z]+[a-z]$'
# print(re.search(pattern, word))
if re.search(pattern, word):
    print('Exactly!')
else:
    print('Try again!')