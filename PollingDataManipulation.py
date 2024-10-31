import pandas as p
import matplotlib.pyplot as mp
import random as r
import numpy as np
import colorsys as c

# Number of Voting Spots in Cities then show its Bar graph 
# Null Laitudes will have the average value through postcode
# Census Tract Average of Each City
# Council District Median through Numpy
# Show in piechart graph grouped by City
#
data = p.read_csv('polling.csv')
votingSpots = data['BOROUGH'].value_counts()
mp.bar(votingSpots.index, votingSpots)
mp.xlabel("Boroughs")
mp.ylabel("Number of voting spots")
mp.show()
data['Latitude'] = data['Latitude'].fillna(data.groupby('POSTCODE')['Latitude'].transform('mean'))
print("Filled Latitudes\n", data['Latitude'])
censusTrackCity = data.groupby('BOROUGH')['Census Tract'].mean()
print("Censor track average of city\n", censusTrackCity)
councilDistrictMedian = np.array(data[data['Council District'].notnull()]['Council District'])
print(f"Median: {np.median(councilDistrictMedian)}")

mp.pie(censusTrackCity, labels=censusTrackCity.index, autopct='%d%%')
mp.legend()
mp.show()

for borough,groupData in data.groupby('BOROUGH'):
    mp.scatter(groupData['Latitude'],groupData['Longitude'],label=borough)
# mp.scatter(x,y,c = [c.hsv_to_rgb(r.random(),r.random(),r.random()) for i in range(100)])
mp.legend()
mp.show()

