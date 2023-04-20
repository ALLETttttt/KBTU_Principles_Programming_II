import datetime
date1 = input('Enter the first date: ')
date2 = input('Enter the second date: ')
year1, month1, day1 = map(int, date1.split('-'))
year2, month2, day2 = map(int, date2.split('-'))
date1 = datetime.datetime(year1, month1, day1)
date2 = datetime.datetime(year2, month2, day2)
total_result = date2 - date1
print(f'In your mentioned date {int(total_result.total_seconds())} seconds!')