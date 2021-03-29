# -*- coding: utf-8 -*-
"""
Grand Projet Semestre 2
Flight Visualisation
"""

import os
from tkinter import*
from tkinter import ttk
from pandas import*
from numpy import*
from matplotlib.pyplot import*

df = read_csv('flight_info.csv', delimiter = ',')

year = df['Year']
month = df['Month']
DayofMonth = df['DayofMonth']
DayofWeek = df['DayOfWeek']
FightDate = df['FlightDate']
FlightNum = df['FlightNum']
OriginAirport = df['OriginAirportID']
OriginCityName = df['OriginCityName']
OriginState = df['OriginState']
OriginStateName = df['OriginStateName']
DestAirportID = df['DestAirportID']
DestCityName = df['DestCityName']
DestState = df['DestState']
DestStateName = df['DestStateName']
DepTime = df['DepTime']
DepDelayMinutes = df['DepDelayMinutes']
ArrTime = df['ArrTime']
ArrDelayMinutes = df['ArrDelayMinutes']
AirTime = df['AirTime']
Distance = df['Distance']

#bar([DestStateName], [FlightNum], color = 'blue')
#show()

a = 0
b = 0
c = 0
d = 0
e = 0
for i in range(len(DestStateName)):
	a = DestStateName[i]
	if a == "Arizona":
		b += 1

	if a == "Texas":
		c += 1

	if a == "Florida":
		d += 1

	if a == "Nevada":
		e += 1	

print(b, c, d, e)

os.system("pause")