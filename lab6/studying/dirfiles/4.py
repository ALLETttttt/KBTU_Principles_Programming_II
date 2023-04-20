filename = "text.txt"
cnt = 0
with open(filename, 'r') as files:
    for i in files:
        cnt += 1
print(f'Amount of lines: {cnt}')