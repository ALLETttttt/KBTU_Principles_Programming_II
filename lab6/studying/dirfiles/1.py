import os
# path = input(r'')
path = r'C:\Users\user\PycharmProjects\week 3\week 3\function2\lab6\studying'
print("Only directories:")
print([direc for direc in os.listdir(path) if os.path.isdir(os.path.join(path, direc))])
print("Only files:")
print([file for file in os.listdir(path) if not os.path.isdir(os.path.join(path, file))])
print("Directories and Files:")
print([dirfile for dirfile in os.listdir(path)])

