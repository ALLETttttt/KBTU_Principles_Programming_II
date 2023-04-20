def filter_prime(x):
    ok = True
    for i in range(2, x):
        if x % i == 0:
            ok = False
            break

    if ok:
        print(x, end=' ')


a = list(map(int, input().split()))
for i in range(len(a)):
    filter_prime(a[i])


