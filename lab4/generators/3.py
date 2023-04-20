from ast import Yield


def f(n):
    for i in range(n):
        if i%3==0 and i%4==0:
            yield i

n = int(input())
print(*f(n), sep = " ")