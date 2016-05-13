#!/usr/bin/python
import sys

all = {}
for line in sys.stdin:
	line = line.strip()
	result = line.split("\t")

	date = result[0]					
	trips = float(result[1])

	if date in all:							
		all[date] += trips		
	else:				
		all[date] = trips
	
for key, value in all.iteritems():	
	year = key[:4]
	totalTrips = "%.0f" %(value)
	
	print key + "," + totalTrips + "," + year