import re

word = input()
qw = 0
for i in range(len(word)):
    if word[i] == '_':
        qw = word[i+1]
        qw = qw.upper()

k = re.sub('[_][a-z]', qw, word)
print(k)
