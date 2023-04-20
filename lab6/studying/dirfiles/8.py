import os
k = "delete.txt"
# with open("delete.txt", "w") as file:
#     file.write()
path = r'C:\Users\user\PycharmProjects\week 3\week 3\function2'
if os.path.exists(path):
    print("Your file is deleted")
    os.remove(k)
else:
    print("Nothing to delete!")
