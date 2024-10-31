import pandas as p
import random as r
import matplotlib.pyplot as mp
import numpy as np

pollingData = p.read_csv('polling.csv',usecols=['BOROUGH','Latitude','Longitude','POSTCODE'])

pollingData['Latitude'].fillna(pollingData['Latitude'].mean(),inplace=True)
pollingData['Longitude'].fillna(pollingData['Longitude'].mean(),inplace=True)
print(pollingData)

pollingStations = pollingData.groupby('BOROUGH').count()
boroughs = pollingStations.index
counts = pollingStations['Latitude']
mp.bar(boroughs,counts,color=['#fb8500','#219ebc','#c1121f','#000212'])
mp.show()
