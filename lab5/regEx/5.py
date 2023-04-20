import re

text = input()
pattern = '^a.*b$'
if re.search(pattern, text):
    print('OK')
else:
    print('no')