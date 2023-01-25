day_in_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
def is_leap(year):
    if year%4 == 0 and (year%100 != 0 or year%400 == 0):
        leap = 1
    else: leap = 0
    return leap
def day_of_year(day,month,year):
    day_of_years = 0
    if is_leap(year)==1:
        day_in_month[2]+=1
    for i in range(1,month):
        day_of_years += day_in_month[i]
    day_of_years += day
    return day_of_years
def day_in_year(y1,y2):
    sum = 0
    for i in range(y1,y2):
        if is_leap(i)==1:
            sum += 366
        else:
            sum+=365
    return sum
def date_diff(date1,date2):
    d1 =list(map(int,date1.split('-')))
    d2 =list(map(int,date2.split('-')))
    date = 0
    if 12<d1[1] or d1[1]<1 or d1[0]>day_in_month[d1[1]] or d2[0]>day_in_month[d2[1]]:
        date = -1
    else:
        date += -day_of_year(d1[0],d1[1],d1[2])+day_of_year(d2[0],d2[1],d2[2])+day_in_year(d1[2],d2[2]) + 1
    return date
           

print(date_diff('0-18-2018', '1-19-2020'))


