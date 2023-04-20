s = input()
cnt1, cnt2 = 0, 0
for i in s:
    if i.isupper():
        cnt1 += 1
    elif i.islower():
        cnt2 += 1

print(f'Amount of upper case: {cnt1}')
print(f'Amount of lower case: {cnt2}')