from datetime import date
from datetime import time
from datetime import datetime

## DATE OBJECTS

# Get today's date from the simple today() method from the date class
today = date.today()
print ("Today's date is ", today)

# print out the date's individual components
print ("Date Components: ", today.day, today.month, today.year)

# retrieve today's weekday (0=Monday, 6=Sunday)
print ("Today's Weekday #: ", today.weekday())

## DATETIME OBJECTS
# Get today's date from the datetime class
today = datetime.now()
print  ("The current date and time is ", today)

# Get the current time
t = datetime.time(datetime.now())
print ("The current time is ", t)

# weekday returns 0 (monday) through 6 (sunday)
wd = date.weekday(today)
# Days start at 0 for Monday
days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
print ("Today is day number %d" % wd)
print ("Which is a " + days[wd])


# --- Formatting ---

# Times and dates can be formatted using a set of predefined string
# control codes
now = datetime.now() # get the current date and time

#### Date Formatting ####

# %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
print(now.strftime("%Y")) # full year with century; "%y" for abbreviated year.
print(now.strftime("%A, %d %B, %y")) # abbreviated day, num, full month, abbreviated year

# %c - locale's date and time, %x - locale's date, %X - locale's time
print(now.strftime("%c"))
print(now.strftime("%x"))
print(now.strftime("%X"))

#### Time Formatting ####

# %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
print(now.strftime("%I:%M:%S %p")) # 12-Hour:Minute:Second:AM
print(now.strftime("%H:%M")) # 24-Hour:Minute


# --- Timedeltas ---

from datetime import timedelta

# construct a basic timedelta and print it
print(timedelta(days=365, hours=5, minutes=1))

# print today's date
print("today is: " + str(datetime.now()))

# print today's date one year from now
print("one year from now it will be: " + str(datetime.now() + timedelta(days=365)))

# create a timedelta that uses more than one argument
print("in two weeks and 3 days it will be: " + str(datetime.now() + timedelta(weeks=2, days=3)))

# calculate the date 1 week ago, formatted as a string
t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d, %Y")
print("one week ago it was " + s)

### How many days until April Fools' Day?

today = date.today()  # get today's date
afd = date(today.year, 4, 1)  # get April Fool's for the same year
# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if afd < today:
    print("April Fool's day already went by %d days ago" % ((today-afd).days))
    afd = afd.replace(year=today.year + 1)  # if so, get the date for next year

# Now calculate the amount of time until April Fool's Day
time_to_afd = abs(afd - today)
print(time_to_afd.days, "days until next April Fools' Day!")
print()
print('I like this!')
import datetime
now = datetime.datetime.now()
print(now.year, now.month, now.day, now.hour, now.minute, now.second)
