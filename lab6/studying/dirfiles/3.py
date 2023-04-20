import os

path = r'C:\Users\user\PycharmProjects\week 3\week 3\function2'
if os.path.exists(path):
    print(f'Your path exists! \nYour path`s filename: {os.path.basename(path)} \nYour path`s directory portion: {os.path.dirname(path)}')
else:
    print("Your path does not exist!")