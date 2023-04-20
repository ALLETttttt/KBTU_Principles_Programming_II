import re

text = 'PythonTheBest'
pattern = '[A-Z][^A-Z]*'
print(re.findall(pattern, text))