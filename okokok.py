import urllib2
import json
import csv
from array import *
import os.path

#queries the API and returns JSON
def query_API(self):
    state = self.state
    city = self.city
    
    queryString = 'http://api.wunderground.com/api/f3cdf122d8571d47/forecast10day/q/'+state+'/'+city+'.json'
    f=urllib2.urlopen(queryString)
    return f

def getJSONData(self):
    f = self.query_API()
    state = self.state
    city = self.city
    #f = urllib2.urlopen('http://api.wunderground.com/api/f3cdf122d8571d47/forecast10day/q/CO/Boulder.json')
    json_string = f.read()
    parsed_json = json.loads(json_string)
    highList= []
    lowList = []
    name = city+state
    for i in range(0, 10):
        highList.append(parsed_json['forecast']['simpleforecast']['forecastday'][i]['high']['fahrenheit'])
        lowList.append(parsed_json['forecast']['simpleforecast']['forecastday'][i]['low']['fahrenheit'])

