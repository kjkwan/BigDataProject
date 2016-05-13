#!/usr/bin/python
import sys


revenues = []

date1 =  "init"
year1 = "0"
for line in sys.stdin:
	line = line.strip()
	result = line.split("\t")

	date2 = result[0]
	revenue = float(result[1])
	year2 = result[2]	

	if date1 == "init":
		revenues.append(revenue)

	elif date1 == date2:	#date2 currently exists; just update revenues list
		revenues.append(revenue)

	else: #date1 != date2 --> date2 is a new date. print the old date and start a new date of revenues
		value = "%.2f" %(sum(revenues))
		print date1 + "\t" + value + "\t" + year1
		revenues = []

	date1 = date2
	year1 = year2

value = "%.2f" %(sum(revenues))
print date1 + "\t" + value + "\t" + year1