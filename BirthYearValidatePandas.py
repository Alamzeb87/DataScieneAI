import pandas as p
import random as r
import xarray as xr

# User Input of length of Students
# User Inputs birth years, names of all students
# Two Series Names , Birth Year
# Combine in a DataFrame
# Students Age calculation and column addition
names = []
birthYears = []
numOfStudents = int(input("Enter number of students"))
for i in range(numOfStudents):
    name = input("Name: ")
    birthYear = int(input("Birth Year: "))
    names.append(name)
    birthYears.append(birthYear)

nameSeries = p.Series(names)
birthYearSeries = p.Series(birthYears)
nameBirthDictionary = {'Names': nameSeries, 'BirthYear':birthYearSeries}
nameBirthYearDT = p.DataFrame(nameBirthDictionary)
nameBirthYearDT['Age'] = 2024 - nameBirthYearDT['BirthYear'] 
nameBirthYearDT['Validate'] = nameBirthYearDT['Age'] >= 18
print(nameBirthYearDT)
