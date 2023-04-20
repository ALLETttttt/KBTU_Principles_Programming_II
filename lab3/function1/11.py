# def palindrome(s):
#     t = s
#     if s[::-1] == t:
#         return True
#     return False
#
#
# q = input()
# print(palindrome(q))


def isPalin(k):
    for i in range(0, len(k)//2):
        if k[i] != k[len(k)-i-1]:
            return False
    return True


k = input()
print(isPalin(k))
