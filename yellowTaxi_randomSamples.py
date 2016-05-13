from random import randint
import csv

def isSampleRow(percentSampled):
	'''
	Returns True a certain percent of the time, as specified by percentSampled.

	Input: Specify the percent of the dataset that you want to sample.
	Output: Boolean True or False
	'''
	return randint(1, 100) < percentSampled


def sampleTaxiData(percentSampled):
	'''
	Samples a specified percentage of the dataset. Saves the sampled data to csv file.
	'''
	years = ["2014"]
	months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

	for year in years:
		for month in months:
			inputFileName = 'yellow_tripdata_%s-%s.csv' %(year, month)
			outputFileName = 'sampleRows_yellow_tripdata_%s-%s.csv' %(year, month)

			inputFile = open(inputFileName, 'rb')
			taxiData = csv.reader(inputFile)

			outputFile = open(outputFileName, 'wb')
			writer = csv.writer(outputFile)
			
			for row in taxiData:
				if(isSampleRow(percentSampled)):
					writer.writerow(row)

			inputFile.close()
			outputFile.close()



percentSampled = 25
sampleTaxiData(percentSampled)