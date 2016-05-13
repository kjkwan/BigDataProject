#!/usr/bin/python
import sys

all = {}  #date,timeOfDayLabel:[totalRevenue, totalTrips]
for line in sys.stdin:
	line = line.strip()
	result = line.split("\t")

	# key = result[0].split(",")
	# date = key[0]
	# year = date[:4]
	# timeOfDayLabel = key[1]

	key = result[0]
	
	revenue = float(result[1])
	trips = float(result[2])

	if key in all: # key already exists, just update the revenue and total trips							
		all[key][0] += revenue
		all[key][1] += trips
	else:				# add new key and value (the revenue)
		all[key] = [revenue, trips]

for key, value in all.iteritems():
	key = key.split(",")	
	date = key[0]
	year = date[:4]
	timeOfDayLabel = key[1]

	totalRevenue = "%.2f" %(value[0])
	totalTrips = "%.0f" %(value[1])
	
	print date + "," + timeOfDayLabel + "," + totalRevenue + "," + totalTrips + "," + year