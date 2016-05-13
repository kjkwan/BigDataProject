#!/usr/bin/python

import sys

def constructRevenue(result, i):	
	fare_amount = float(result[-6+i])	
	if fare_amount < 0: fare_amount = float(0)

	tip = float(result[-3+i])
	if tip < 0: tip = float(0)

	surcharge = float(result[-5+i])	
	if surcharge < 0: surcharge = float(0)
	
	return (fare_amount + tip + surcharge)
	
def determine_i(numCols):
	if numCols == 19: return -1 #2015 data
	else: return 0 # numCols == 18 for 2009-2014 data


dict_all = {}	# consists of the key (date, lon, lat) and a list of the revenues that key
				
for line in sys.stdin:
	line = line.strip()

	if not(line == ''):
		result = line.split(",")
		numCols = len(result)		

		if numCols >= 18:									# ignore the incomplete entries
			if not(result[-1].strip() == 'total_amount'):	# ignore header		
				if not(result[-1].strip() == 'Total_Amt'):	# ignore a different variation of the header
					# used to account for incremented indexing for year 2015, which has one more column than the years 2009-2014
					i = determine_i(numCols)

					date = result[-17+i][:10]					# key
					year = date[:4]								# part of value
					pickupLon = round(float(result[-13+i]), 3)	# round coordinate to 3 decimal places
					pickupLat = round(float(result[-12+i]), 3)	# round coordinate to 3 decimal places

					if not((pickupLon == 0) or (pickupLat == 0)):		# filter out the zero lat lon coordinates			
						key = date + "," + str(pickupLon)+ "," + str(pickupLat)

						if (year == "2010") and numCols == 19: i = 0	# accounts for a column of blanks in the middle of some of the 2010 data
						
						revenue = constructRevenue(result, i)	# part of value							

						if key in dict_all: # key already exists, just update the revenue and total trips							
							dict_all[key].append(revenue)
						else:				# add new key and value (the revenue)
							dict_all[key] = [revenue]

						
for key, value in dict_all.iteritems():
	totalTrips = str(len(value))
	totalRevenue = "%.2f" %sum(value)
	
	print key + "\t" + totalRevenue + "\t" + totalTrips

# key: date, lon, lat
# value: sum of revenue, total number of trips