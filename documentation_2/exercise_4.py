# Date

# 4. Using the datetime module in Python, how would you obtain the current date and time?


# https://docs.python.org/3/library/datetime.html

# class datetime.datetime
# A combination of a date and a time. Attributes: year, month, day, hour, minute, second, microsecond, and tzinfo.

from datetime import datetime

today = datetime.now()
print(today)
# 2025-04-05 20:52:06.249749