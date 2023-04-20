from itertools import permutations

def permut(x):
    x = permutations(x)
    for i in x:
        print(i)


a = list(map(int, input().split()))
permut(a)



# a = list(map(int, input().split()))
# permut = permutations(a)
# for i in list(permut):
#     print(i)