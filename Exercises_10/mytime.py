"""
 Script: mytime.py
 By: Shivani Gupta (L00171176)
 Tested: Python v3.10.7; Windows 11
 Date: 30th October, 2022
"""

from datetime import datetime as dt

#get current date time
today = dt.now()
print(f"Current date-time : {today}")

#get unix time
unix_epoch_time = dt.timestamp(today)
#print(unix_epoch_time)

#date and day using strftime
weekday = dt.now().strftime("%A")
month = dt.now().strftime("%B")
year = dt.now().strftime("%Y")
date = dt.now().strftime("%d")

#time using strftime
hour = dt.now().strftime("%I")
ampm = dt.now().strftime("%p")
minute = dt.now().strftime("%M")
second = dt.now().strftime("%S")

print(f"Date : {date} {month},{year}, {weekday}")
print(f"Time : {hour}:{minute}:{second} {ampm}")