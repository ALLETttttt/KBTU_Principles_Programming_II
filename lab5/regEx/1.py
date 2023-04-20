import re

txt = input()
pattern = 'a(b*)$'
if re.search(pattern, txt):
    print('Found matches')
else:
    print('No matches')