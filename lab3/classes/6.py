# def check_prime(n):
#     for i in range(n):
#         if i == 0 or i == 1:
#             continue
#         if n % i == 0:
#             return False
#     return True
#
#
# a = list(map(int, input().split()))
# print(list(filter(lambda x: check_prime(x), a)))


def check_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


a = list(map(int, input().split()))
result = list(filter(lambda x: check_prime(x), a))
print(*result)