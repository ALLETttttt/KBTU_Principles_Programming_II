def spy_game(n):
    string = ''
    for i in n:
        if i == '0' or i == '7':
            string += i
        if '007' in string:
            return True
    return False


arr = list(map(str, input().split(',')))
print(spy_game(arr))

