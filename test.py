#!/usr/bin/python
print "Give the year of your birth!"
year = int(raw_input("Year o'birth!"))
month = int(raw_input("An' mon' o'birth?"))
day = int(raw_input("An' which day yer mother..."))
curr_time = time.localtime()
age = curr_time.tm_year - year
if month > curr_time.tm_month or (month == curr_time.tm_month and day > curr_time.tm_day):
	age=-1
print "Since " + age + " yer shipping roun' the globe!"
