#!/usr/bin/python

import sys

def constructRevenue(result, i):	
	fare_amount = float(result[-6+i])	
	if fare_amount < 0: fare_amount = float(0)

	tip = float(result[-3+i])
	if tip < 0: tip = float(0)

	surcharge = float(result[-5+i])	
	if surcharge < 0: surcharge = float(0)

	# return "%.2f" %(fare_amount + tip + surcharge)
	return (fare_amount + tip + surcharge)


def constructTimeOfDayLabel(result, dateTime):
	hour = dateTime[-8:-6]

	nightHours = ['00', '01', '02', '03', '04', '05']
	morningHours = ['06', '07', '08', '09', '10', '11']
	afternoonHours = ['12', '13', '14', '15', '16', '17']
	eveningHours = ['18', '19', '20', '21', '22', '23']

	timeOfDayLabel = ""
	if hour in nightHours: timeOfDayLabel = "night"
	elif hour in morningHours: timeOfDayLabel = "morning"
	elif hour in afternoonHours: timeOfDayLabel = "afternoon"
	else: timeOfDayLabel = "evening"

	#print "hour: %s, dayLabeltimeOfDayLabel: %s" %(hour, timeOfDayLabel)
	return timeOfDayLabel

def determine_i(numCols):
	if numCols == 19: return -1 #2015 data
	else: return 0 # numCols == 18 for 2009-2014 data

all = {} #key:value is date,timeOfDayLabel:list of revenues
for line in sys.stdin:
	line = line.strip()

	if not(line == ''):							# ignore blank lines
		result = line.split(",")
		numCols = len(result)		

		if numCols >= 18:									# ignore the incomplete entries
			if not(result[-1].strip() == 'total_amount'):	# ignore header		
				if not(result[-1].strip() == 'Total_Amt'):	# ignore a different variation of the header
					# used to account for incremented indexing for year 2015, which has one more column than the years 2009-2014
					i = determine_i(numCols)

					dateTime = result[-17+i]
					date = dateTime[:10]				# key
					year = date[:4]				

					timeOfDayLabel = constructTimeOfDayLabel(result, dateTime) #value1

					if (year == "2010") and numCols == 19: i = 0	# accounts for a column of blanks in the middle of some of the 2010 data								
					revenue = constructRevenue(result, i)	# value2						
					
					key = date + "," + timeOfDayLabel
					
					if key in all: # key already exists, just update the revenue and total trips							
						all[key].append(revenue)
					else:				# add new key and value (the revenue)
						all[key] = [revenue]

for key, value in all.iteritems():
	totalTrips = str(len(value))
	totalRevenue = "%.2f" %sum(value)
	
	print key + "\t" + totalRevenue + "\t" + totalTrips