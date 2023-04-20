import os
print(os.getcwd())
path = r'C:\Users\user\PycharmProjects\week 3\week 3\function2'
direc = os.listdir(path)
for i in direc:
    print(i)
    print('Exist:', os.access(path, os.F_OK))
    print('Readable:', os.access(path, os.R_OK))
    print('Writable:', os.access(path, os.W_OK))
    print('Executable:', os.access(path, os.X_OK))


