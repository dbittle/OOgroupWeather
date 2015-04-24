import csv
from array import *
import time
import timer


class Analyze_Data:
	cities = (("Boulder", "CO"))
	name = 'BoulderCO' #************************************************
	
	def readFromForecast(self):
		name = self.name
		rowCount = 0
		forecastVals = []
		numCol = 10
		with open(name+"high.csv", 'rb') as csvfile:
			numRows = sum(1 for row in csvfile)
			print numRows
			
		with open(name+"high.csv", 'rb') as csvfile:
			fieldnames = ['1','2','3','4','5','6','7','8','9','10','date']
			dr = csv.DictReader(csvfile, fieldnames=fieldnames)
			for row in dr:
				rowCount = rowCount + 1
				if (rowCount >= numRows - 9):
					val = row[str(numCol)] #10 days out should be yesterday, sleep at the beginning of forecast pull?
					#[val] + forecastVals
					forecastVals.append(val)
					print str(numCol)
					numCol = numCol - 1;
					print rowCount
		forecastVals.reverse()
		print forecastVals
		return forecastVals

				
		
	def readFromObserved(self):
		name = self.name
		rowCount = 0
		observedVal = 0
		with open(name+"_Observed.csv", 'r') as csvfile:
			numRows = sum(1 for row in csvfile)
			print numRows
			
		with open(name+"_Observed.csv", 'r') as csvfile:
			fieldnames = ['Hi', 'Lo', 'Date']
			reader = csv.DictReader(csvfile, fieldnames=fieldnames)
			for row in reader:
				rowCount = rowCount + 1
				if (rowCount >= numRows):
					observedVal = row['Hi']
					print rowCount
					print observedVal
					return observedVal
					
	def performAnalysis(self, temp, forecast):
		name = self.name
		accuracyByDay = []
		predictedByDay = forecast
		predictedByDay.reverse()
		numRows = 0
		for x in forecast:
			acc = abs((float(x)/float(temp))-1)*100
			acc = round(acc, 2)
			print acc
			accuracyByDay.append(acc)
		accuracyByDay.reverse()
		print accuracyByDay
		with open(name+"analysis.csv", 'r') as csvfile:
			fieldnames = ['days-out', 'predicted', 'observed', 'percent-off', 'date-observed']
			numRows = sum(1 for row in csvfile)
			
		with open(name+"analysis.csv", 'a') as csvfile:
			fieldnames = ['days-out', 'predicted', 'observed', 'percent-off', 'date-observed']
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			if (numRows == 0): #change?
				writer.writeheader()
			daysOut = 10
			for x in accuracyByDay:
				grabDay = abs(daysOut-10)
				writer.writerow({'days-out': str(daysOut), 'predicted': predictedByDay[grabDay], 'observed': temp, 'percent-off': x})
				daysOut = daysOut - 1
				
			

			
			
#****test****
x = Analyze_Data()	
x.readFromForecast()
observedTemp = x.readFromObserved()
print observedTemp + " is the observed temp"
forecastTemps = x.readFromForecast()
print forecastTemps

x.performAnalysis(observedTemp, forecastTemps) 







