import calendar
import time

current_GMT = time.gmtime()

time_stamp = calendar.timegm(current_GMT)
print("Current timestamp:", str(time_stamp)+10)
