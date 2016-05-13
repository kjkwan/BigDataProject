#!/usr/bin/python
import sys


# assumes input is the output from reduceDayLabelRevenue.py

all = {}			#key:totalTrips

for line in sys.stdin:
	line = line.strip()
	result = line.split(",")

	date = result[0]			#key	
	trips = float(result[3])	#value

	if date in all: # key already exists, just update the revenue and total trips							
		all[date] += trips		
	else:				# add new key and value (the revenue)
		all[date] = trips

for key, value in all.iteritems():	
	totalTrips = "%.0f" %(value)
	
	print key + "\t" + totalTrips