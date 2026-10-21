import datetime

current = datetime.datetime.now()

print("Current date:", current.date())
print("Current time:", current.strftime("%H:%M:%S"))

print("Year:", current.year)
print("Month:", current.month)
print("Day:", current.day)
