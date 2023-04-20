def solve(heads, legs):
    if heads >= legs:
        print('Error')
    elif legs % 2 != 0:
        print('Error')
    else:
        rabbit = (legs - 2*heads)/2
        chicken = heads - rabbit
        print(f'Amount of chicken: {int(chicken)}')
        print(f'Amount of rabbit: {int(rabbit)}')


solve(35, 94)
