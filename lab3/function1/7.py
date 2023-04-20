def has_33(num):
    for i in range(len(num)-1):
        if num[i] == 3 and num[i+1] == 3:
            return True
    return False


arr = list(map(int, input().split()))
print(has_33(arr))



