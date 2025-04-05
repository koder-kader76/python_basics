# Which Year is This?

# 5. The Python documentation for the datetime module provides two attributes to retrieve the year from a date or datetime object: year and isocalendar.

from datetime import date

today = date.today()

today_year = today.year
iso_year = today.isocalendar()[0]

print(today_year)
print(iso_year)

# What is the difference between the year attribute and the isocalendar method?

#  the year attribute returns the year between MINYEAR (1) & MAXYEAR (9999)
# the isocalender attribute returns a tuple with (year, week, day) - so it is necessary to retrieve the year by using index 1