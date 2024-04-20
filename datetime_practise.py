#TO WORK WITH DATE AND TIME PYTHON HAVE A MODULE CALLED AS "DATETIME MODULE"
import datetime
#1)To print current date and time:
# import datetime                #in datetime module all libraries related to date and time are contained.
# print(datetime.datetime.now()) #output:-2022-10-02 08:40:00.399327

# from datetime import datetime #2nd method   #datetime is a class 
# print(datetime.now())      #output:2022-10-02 08:43:10.299740

#2) if we want to print only date
# from datetime import date
# print(date.today())  #output: 2022-10-02

# import datetime
# print(datetime.date.today()) #2022-10-02
# print("today's date is:" , datetime.date.today()) #output:-today's date is: 2022-10-02
# datetime.date Class
# You can instantiate date objects from the date class.A date object represents a date (year, month and day).

#3)to represent date
# a=datetime.date(2022,10,2)
# print(a) #output:-2022-10-02  This class will print the date in year-month-date format

# b=datetime.date(1999,2,24) #this class takes 3 arguments that is year month and date
# print(b) #output:-1999-02-24

#4)Get date from a timestamp 
b=datetime.date.fromtimestamp(1020304040)
print(b) #Output:-2002-05-02

#6)Print today's year, month and day
# today=datetime.date.today()
# print("current year is =" ,today.year)
# print("current month is =",today.month)
# print("current day is =",today.day)    
# Output:-current year is = 2022
# current month is = 10
# current day is = 2

#7)to represent time:
# a=datetime.time()
# print(a)   Output:-00:00:00

# b=datetime.time(1,24,24) #we can represent time by passing the hour minute and seconds as arguments
# print("time is:",b) Output:-time is: 01:24:24

# z=datetime.time(hour=11,minute=40,second=4,microsecond=3542)
# print(z)  Output:-11:40:04.003542

#8)Print hour, minute, second 
# v=datetime.time(9,30,23)
# print("hour =",v.hour)
# print("minute =",v.minute)
# print("second =",v.second)
# Output:-
# hour = 9
# minute = 30
# second = 23

# datetime.datetime
# The datetime module has a class named dateclass that can contain information from both date and time objects.

# v=datetime.datetime(1999,2,24,1,25,23)
# print(v)  Output:1999-02-24 01:25:23

#9)Print year, month, hour, minute and 
# z=datetime.datetime(2022,10,2,1,28,12,231224)
# print("year :", z.year)
# print("month:", z.month)
# print("day:",z.day)
# print("hour :", z.hour)
# print("minute :", z.minute)
# print("second :", z.second)
# print("microsecond:",z.microsecond)

#output:-2002-05-02
# year : 2022
# month: 10
# day: 2
# hour : 1
# minute : 28
# second : 12
# microsecond: 231224

#10)datetime.timedelta:-A timedelta object represents the difference between two dates or times.

from datetime import datetime, date

# date1= date(year = 2022, month = 7, day = 12)
# date2= date(year = 2010, month = 1, day = 31)
# date_difference= date1-date2
# print("difference between date is =" , date_difference) #Output:-difference between date is = 4545 days, 0:00:00

#11)Difference between two timedelta objects
from datetime import timedelta
# td1 = timedelta(weeks = 6, days = 5, hours = 1, seconds = 33)
# td2= timedelta(days = 30, hours = 6, minutes = 44, seconds = 54)
# tdd = td1 - td2

# print("tdd =", tdd)  #Output:-tdd = 16 days, 18:15:39

# #12)Time duration in seconds
# t = timedelta(days = 31, hours = 12, seconds = 53, microseconds = 233423)
# print("total seconds =", t.total_seconds()) #Output:-total seconds = 2721653.233423

#13) Format date using strftime()
from datetime import datetime
# now=datetime.now()
# t = now.strftime("%H:%M:%S")
# print("time:", t) Output:-time: 14:02:08


# z=now.strftime("%H:%M:%S , %Y-%m-%d")
# print(z) Output:-14:02:08 , 2022-10-02

#14)strptime()
# b = "24 February, 1999"
# print("date_string =", b) Output:-date_string = 24 February, 1999

