def multiply(arr):
    res = 1
    for i in range(len(arr)):
        res *= arr[i]
    return res

arr = list(map(int, input().split()))
print(multiply(arr))

# from functools import reduce
# print(reduce((lambda x, y: x*y), list(map(int, input().split()))))

# from functools import reduce 
# import operator
# arr = list(map(int, input().split()))
# print(reduce(operator.mul, (arr), 1))
