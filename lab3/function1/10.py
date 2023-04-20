def unique(a):
    gg = []
    a.sort()
    for i in range(len(a)-1):
        if a[i] != a[i+1]:
            gg.append(a[i])
        else:
            continue
    gg.append(a[len(a)-1])

    print(*gg)


arr = list(map(int, input().split()))
unique(arr)
