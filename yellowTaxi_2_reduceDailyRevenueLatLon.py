#!/usr/bin/python
import sys



for line in sys.stdin:
	line = line.strip()
	result = line.split("\t")

	key = result[0].split(",")	
	date = key[0]
	lon = key[1]
	lat = key[2]

	year = date[:4]	
	
	revenue = result[1]
	numTrips = result[2]
						

	print date + "," + lon + "," + lat + "," + revenue + "," + numTrips + "," + year