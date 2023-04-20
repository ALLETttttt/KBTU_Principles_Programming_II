def squares(a, b):
    for i in range(a, b+1):
        yield i*i

a = int(input())
b = int(input())
if a > b:
    print('Error')
else:
    print(*squares(a, b))