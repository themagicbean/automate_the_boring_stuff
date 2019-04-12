'''
Created on Apr 8, 2019

@author: darrenbean
'''
import time
import datetime

datetime.datetime.now()
print(datetime.datetime(2015, 2, 27, 11, 10, 49, 55))
# could not use last argv in ABSWP b/c not "tzinfo" 
dt = datetime.datetime(2015, 10, 21, 16, 29, 0)
print(str(dt.year) + "/" + str(dt.month) + "/" + str(dt.day))
print(dt.year, dt.month, dt.day)
print(str(dt.hour) + ":" + str(dt.minute) + ":" + str(dt.second))
print(dt.hour, dt.minute, dt.second)

print(time.time())
print(datetime.datetime.fromtimestamp(time.time()))

delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
print(delta.total_seconds())
print(str(delta))

print(dt + delta)

"""
halloween2020 = datetime.datetime(2020, 10, 31)
while datetime.datetime.now() < halloween2020:
    time.sleep(1)
"""

#strftime = convert datetime to readable strings
print(dt.strftime('%Y/%m/%d %H:%M:%S'))
print(dt.strftime("%B of '%y"))

#strptime = get datetime from strings
print(datetime.datetime.strptime('October 21, 2015', '%B %d, %Y'))
print(datetime.datetime.strptime("November of '63", "%B of '%y"))
#goes forward to 2063 bc Unix epoch started in 1970 so no 1963
