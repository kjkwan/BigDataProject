#!/usr/bin/python

import sys

def constructRevenue(result, i):	
	fare_amount = float(result[-6+i])	
	if fare_amount < 0: fare_amount = float(0)

	tip = float(result[-3+i])
	if tip < 0: tip = float(0)

	surcharge = float(result[-5+i])	
	if surcharge < 0: surcharge = float(0)

	return "%.2f" %(fare_amount + tip + surcharge)
	
def determine_i(numCols):
	if numCols == 19: return -1 #2015 data
	else: return 0 # numCols == 18 for 2009-2014 data


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

					date = result[-17+i][:10]				# key
					year = date[:4]							# value2

					if (year == "2010") and numCols == 19: i = 0	# accounts for a column of blanks in the middle of some of the 2010 data
					
					revenue = constructRevenue(result, i)	# value1
					
					print date + "\t" + revenue + "\t" + year

