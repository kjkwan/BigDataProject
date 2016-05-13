#!/usr/bin/python
import sys



all = {}	#key:value is date:totalTrips
for line in sys.stdin:
	line = line.strip()
	result = line.split("\t")

	date = result[0]					
	trips = float(result[1])

	if date in all: # key already exists, just update the revenue and total trips							
		all[date] += trips		
	else:				# add new key and value (the revenue)
		all[date] = trips
	
for key, value in all.iteritems():	
	year = key[:4]
	totalTrips = "%.0f" %(value)
	
	print key + "," + totalTrips + "," + year