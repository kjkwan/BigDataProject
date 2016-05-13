import pandas as pd
from googlemaps import GoogleMaps

lookup = pd.read_csv('taxi-zone-lookup.csv')
data = pd.read_csv('uber-raw-data-janjune-15.csv')

df_new = pd.merge(lookup, data, on='locationID')

list_name = df_new.["Borough"].tolist()

for name in list_name
	gmaps = GoogleMaps("AIzaSyAoj9_phbO7tsQTS66U3dCDjUG37z0EK3M")
	address = name
	lat, lng = gmaps.address_to_latlng(address)
	print lat, lng