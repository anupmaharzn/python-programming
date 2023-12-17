import datetime

mytime = datetime.time(1,20)

print(mytime.minute)
print(mytime.hour)

print(mytime)
print(type(mytime))


today = datetime.date.today()

print(today)

print(today.year)
print(today.month)
print(today.day)
print(today.ctime())


from datetime import datetime


mydatetime = datetime(2021,10,3,14,12,1)

print(datetime)
print(mydatetime)
print(mydatetime.year)


from datetime import date,datetime

date1  = date(2021,11,3)
date2 = date(2020,11,2)

result = date1 - date2

print(type(result)) #datetime.timedelta object

print(result.days)


datetime1 = datetime(2021,11,3,22,0)
datetime2 = datetime(2020,11,2,12,0)

result = datetime1 - datetime2

print(result)
print(result.seconds)
