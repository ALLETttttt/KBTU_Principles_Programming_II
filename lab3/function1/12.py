def histogram(a):
    for i in range(len(a)):
        print(*['*']*a[i], sep='')


a = list(map(int, input().split()))
histogram(a)