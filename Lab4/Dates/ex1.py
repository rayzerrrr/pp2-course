#1
# from datetime import datetime, timedelta
# dt = datetime.now() - timedelta(days=5)
# print('Current Date :',datetime.now())
# print('5 days before Current Date :',dt)

#2
# from datetime import date
# from datetime import timedelta

# today = date.today()
# print("Today is: ", today)
 
# yesterday = today - timedelta(days = 1)
# print("Yesterday was: ", yesterday)

# tomorrow =today +timedelta(days=1)
# print("Tomorrow: ",tomorrow)


#3
# import datetime
# print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

#4

# from datetime import datetime

# def date_diff_in_seconds(dt2, dt1):
#     delta = dt2 - dt1
#     return int(delta.total_seconds())

# date1 = datetime.strptime('2017-09-01 00:00:00', '%Y-%m-%d %H:%M:%S')

# date2 = datetime.now()

# print("{} seconds".format(date_diff_in_seconds(date2, date1)))
