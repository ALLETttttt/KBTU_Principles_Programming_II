n = int(input())
c = (i**2 for i in range(1, n+1))
print(*c)