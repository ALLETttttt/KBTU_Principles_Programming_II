import string
alphabet = string.ascii_uppercase
for i in alphabet:
    with open(i + ".txt", "w") as file:
        file.write(i)


# import os
# for i in alphabet:
#     os.remove(i + ".txt")
