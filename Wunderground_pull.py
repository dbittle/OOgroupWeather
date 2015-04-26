try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
import json
import csv
from array import *
import time
import os.path
from Api_Pull import Api_Pull

#timer class is subject.
#wunderground_pull is observer
#cities that we want to pull on New York, Los Angeles, Ardmore, Aurora, Honolulu, Boulder
#
#csv for observerved BoulderCO_Observed
#CitySTATE_Observed will be name of CSV

#.keys() vital for parsing through json

class Wunderground_pull(Api_Pull):      
    listofCities = (("New_York",'NY'),("Los_Angeles","CA"),("Ardmore","PA"),("Honolulu","HI"),("Boulder","CO"),("Aurora","CO"))
        
    #queries the API and returns JSON
    def query_API(self,city,state):
        #state = self.state
        #city = self.city
        queryString = 'http://api.wunderground.com/api/f3cdf122d8571d47/forecast10day/q/'+state+'/'+city+'.json'
        tenDay=urllib2.urlopen(queryString)
        queryString = 'http://api.wunderground.com/api/f3cdf122d8571d47/yesterday/q/'+state+'/'+city+'.json'
        yesterday = urllib2.urlopen(queryString)
        return(tenDay,yesterday)
        
        
    #renaming this to UPDATE to comply with observer pattern
    #adding city and state as arguments instead of attributes of API pull
    def get_JSON(self, city, state):
        #state = self.state
        #city = self.city
        #f = urllib2.urlopen('http://api.wunderground.com/api/f3cdf122d8571d47/forecast10day/q/CO/Boulder.json')

        highList= []
        lowList = []
        name = city+state
        tenDayYesterday = self.query_API(city,state)
        tenDay = tenDayYesterday[0]
        yesterday = tenDayYesterday[1]
        
        json_string = yesterday.read()
        parsed_json = json.loads(json_string)

        yesterdayHigh = (parsed_json['history']['dailysummary'][0]['maxtempi'])
        yesterdayLow = (parsed_json['history']['dailysummary'][0]['mintempi'])

        datePulledYesterday = (str(parsed_json['history']['dailysummary'][0]['date']['mon'])+
              str(parsed_json['history']['dailysummary'][0]['date']['mday'])+
              str(parsed_json['history']['dailysummary'][0]['date']['year']))
        
        
        
        if(not(os.path.isfile(name+'_Observed.csv'))):
            print("Creating new observed csv file")
            with open(name+'_Observed.csv', 'w') as csvfile:
                fieldnames = ['hi', 'lo','date']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'hi': yesterdayHigh,'lo': yesterdayLow, 'date': datePulledYesterday})

        
        else:
            shouldRun = True
            with open(name+"_Observed.csv", 'rb') as csvfile:
                fieldnames = ['hi', 'lo','date']
                reader = csv.DictReader(csvfile, fieldnames=fieldnames)
                for row in reader:
                    if(row['date']== datePulledYesterday):
                        print("this date has already been read in")
                        shouldRun = False
        
            if(shouldRun):
                print("Appending to an existing CSV file")
                with open(name+"_Observed.csv", 'a') as csvfile:
                    fieldnames = ['hi', 'lo','date']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writerow({'hi': yesterdayHigh,'lo': yesterdayLow, 'date': datePulledYesterday})
        
            else:
                print("you tried to run the query on this city twice in one day")
        
        #whether to append to the file or write to the file ensures there is only one set of CSVs per city
        #singleton essentially
        json_string = tenDay.read()
        parsed_json = json.loads(json_string)

        time.sleep(180)
        for i in range(0, 10):
            highList.append(parsed_json['forecast']['simpleforecast']['forecastday'][i]['high']['fahrenheit'])
            lowList.append(parsed_json['forecast']['simpleforecast']['forecastday'][i]['low']['fahrenheit'])
        
        datePulled = (str(parsed_json['forecast']['simpleforecast']['forecastday'][0]['date']['month'])+
              str(parsed_json['forecast']['simpleforecast']['forecastday'][0]['date']['day'])+
              str(parsed_json['forecast']['simpleforecast']['forecastday'][0]['date']['year'])) 
 
        
        
        if(not(os.path.isfile(name+"high.csv"))):
            print("Creating new csv files")
            with open(name+"high.csv", 'w') as csvfile:
                fieldnames = ['1', '2','3','4','5','6','7','8','9','10','date']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'1': highList[0],'2': highList[1], '3': highList[2], '4': highList[3],
                 '5': highList[4], '6': highList[5], '7': highList[6],'8': highList[7],'9': highList[8],'10': highList[9],'date':datePulled})
                
            with open(name+"low.csv", 'w') as csvfile:
                fieldnames = ['1', '2','3','4','5','6','7','8','9','10','date']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames) 
                writer.writeheader()
                writer.writerow({'1': lowList[0],'2': lowList[1], '3': lowList[2], '4': lowList[3],
             '5': lowList[4], '6': lowList[5], '7': lowList[6],'8': lowList[7],'9': lowList[8],'10': lowList[9],'date':datePulled})
                
        else:
            shouldRun = True
            with open(name+"high.csv", 'rb') as csvfile:
                fieldnames = ['1', '2','3','4','5','6','7','8','9','10','date']
                reader = csv.DictReader(csvfile, fieldnames=fieldnames)
                for row in reader:
                    if(row['date']== datePulled):
                        print("this date has already been read in")
                        shouldRun = False
                    #print ', '.join(row)
            
            
            
            if(shouldRun):
                print("Appending to an existing CSV file")
                with open(name+"high.csv", 'a') as csvfile:
                    fieldnames = ['1', '2','3','4','5','6','7','8','9','10','date']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writerow({'1': highList[0],'2': highList[1], '3': highList[2], '4': highList[3],
                     '5': highList[4], '6': highList[5], '7': highList[6],'8': highList[7],'9': highList[8],'10': highList[9],'date':datePulled})
            
                with open(name+"low.csv", 'a') as csvfile:
                    fieldnames = ['1', '2','3','4','5','6','7','8','9','10','date']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames) 
                    writer.writerow({'1': lowList[0],'2': lowList[1], '3': lowList[2], '4': lowList[3],'5': lowList[4], '6': lowList[5], '7': lowList[6],'8': lowList[7],'9': lowList[8],'10': lowList[9],'date':datePulled})
            
            #else:
                #print("you tried to run the query on this city twice in one day")

#test Case


#queries all the cities in our list of cities
    def update(self,listofCities):
        #listofCities = (("New_York",'NY'),("Los_Angeles","CA"),("Ardmore","PA"),("Honolulu","HI"),("Boulder","CO"),("Aurora","CO"))
        for x in range(0,(len(listofCities))):
            #x= Wunderground_pull('Wunderground',listofCities[x][0],listofCities[x][1])
            self.get_JSON(listofCities[x][0],listofCities[x][1])
            time.sleep(10)

#x = Wunderground_pull("Wunderground")

#listofCities = (("New_York",'NY'),("Los_Angeles","CA"),("Ardmore","PA"),("Honolulu","HI"),("Boulder","CO"),("Aurora","CO"))
#x.update(listofCities)

#x= Wunderground_pull('Wunderground','Honolulu','HI')
#x.getJSONData()
