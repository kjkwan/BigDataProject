import pandas as pd


def checkColumnNames(year):
	'''
	Checks to make sure the column names are the same for each yellow taxi data file.
	Prints the results of the check. If there are mismatches, the mismatched months are printed.

	input: year as a string	
	'''
	months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

	columnNames1 = ['vendor_id', 'pickup_datetime', 'dropoff_datetime', 'passenger_count',
	 'trip_distance', 'pickup_longitude', 'pickup_latitude', 'rate_code',
	 'store_and_fwd_flag', 'dropoff_longitude', 'dropoff_latitude', 'payment_type',
	 'fare_amount', 'surcharge', 'mta_tax', 'tip_amount', 'tolls_amount',
	 'total_amount']

	mismatchedColumns = []
	previousMonth = "00"
	for i in months:
		fileName = 'yellow_tripdata_%s-%s.csv' %(year, i)

		size = 1
		df = pd.read_csv(fileName, chunksize=size)
		data = pd.DataFrame()
		data = data.append(df.get_chunk(size))

		columnNames2 = data.columns.values

		if not(set(columnNames1) == (set(columnNames1) & set(columnNames2))): 
			mismatch = [previousMonth, i]
			mismatchedColumns.append(mismatch)
			
		columnNames1 = columnNames2
		previousMonth = i

	if len(mismatchedColumns) <= 0:
		print "All files for the year %s have the same column names." %year

	else:
		print "There are column name discrepancies between the following file months:"	
		print mismatchedColumns


checkColumnNames("2014")