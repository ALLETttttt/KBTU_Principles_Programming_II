n = int(input())
"""def f(n):
    while n>=0:
        if n%2==0:
            yield n
        n-=1"""

def fun(n):
    for i in range(n+1):
        if i%2==0:
            yield i

print(*fun(n), sep=", ")