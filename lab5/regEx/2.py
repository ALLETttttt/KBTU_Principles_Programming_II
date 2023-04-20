import re

text = input()
pattern = 'a(b{2}|b{3})$'
if re.search(pattern, text):
    print('YES')
else:
    print('NO')