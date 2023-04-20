import re

text = input()
pattern = '^[a-z]+_[a-z]+$'
if re.search(pattern, text):
    print('Good job!')
else:
    print('Empty!')
