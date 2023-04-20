file = open("sample.txt", "r")
text = file.readlines()
file.close()

file = open("second.txt", "w")
for i in text:
    file.write(i)
file.close()
print('File Copied Successfully!')