from datetime import datetime

def date_diff_in_seconds(dt2, dt1):
    delta = dt2 - dt1
    return int(delta.total_seconds())


date1 = datetime.strptime('2017-09-01 00:00:00', '%Y-%m-%d %H:%M:%S')

date2 = datetime.now()

print("{} seconds".format(date_diff_in_seconds(date2, date1)))
