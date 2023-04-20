import re


text = 'PythonTheBest'
# a = "_".join(re.sub(r'(\w)([A-Z])', r'\1_\2', text).split()).lower()
a = re.sub(r'(\w)([A-Z])', r'\1_\2', text).lower()

print(a)
