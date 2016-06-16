import time
print(time.localtime())
'''time.struct_time(tm_year=2020, tm_mon=2, tm_mday=23, tm_hour=22, 
	tm_min=18, tm_sec=39, tm_wday=0, tm_yday=73, tm_isdst=0)'''
t=time.localtime()
year=t[0]
month=t[1]
day=t[2]
hour=t[3]
minute=t[4]
second=t[5]
print(year)
print(month)
print(day)
print(hour)
print(minute)
print(second)