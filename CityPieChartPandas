import pandas as p
import random as r
import matplotlib.pyplot as mp

# User Input City Name
# property type Pie Chart
properties = p.read_csv('property.csv',usecols=["city","property_type"])
cityName = input("Enter city name: ")
cityProperties = properties[properties.city == cityName]
numberOfHouses = len(cityProperties[cityProperties.property_type == "House"])
numberOfFlates = len(cityProperties[cityProperties.property_type == "Flat"])
mp.pie([numberOfHouses,numberOfFlates],labels = ["Num of Houses","Number of Flats"], autopct='%d%%')
mp.legend()
mp.show()
