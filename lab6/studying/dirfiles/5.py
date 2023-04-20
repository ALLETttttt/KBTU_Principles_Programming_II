output_file = open('months.txt', 'w')
months = ['January', 'February', 'March', 'April']
for month in months:
    output_file.write(month + '\n')

output_file.close()