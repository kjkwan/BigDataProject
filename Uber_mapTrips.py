#!/usr/bin/python
import sys

all = {}
for line in sys.stdin:
	line = line.strip()
	result = line.split(",")

	date = result[0]			
	trips = float(result[3])	

	if date in all: 						
		all[date] += trips		
	else:				
		all[date] = trips

for key, value in all.iteritems():	
	totalTrips = "%.0f" %(value)
	
	print key + "\t" + totalTrips