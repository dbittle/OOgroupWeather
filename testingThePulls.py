try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
import json
import csv
from array import *
import os.path
from Api_Pull import Api_Pull


queryString = 'http://api.wunderground.com/api/f3cdf122d8571d47/yesterday/q/CO/Denver.json'
yesterday = urllib2.urlopen(queryString)
json_string = yesterday.read()
parsed_json = json.loads(json_string)

#['observations']

#for key in parsed_json['history']['dailysummary'].keys():
    #print key


print(parsed_json['history']['dailysummary'][0]['maxtempi'])
print(parsed_json['history']['dailysummary'][0]['mintempi'])

datePulled = (str(parsed_json['history']['dailysummary'][0]['date']['mon'])+
              str(parsed_json['history']['dailysummary'][0]['date']['mday'])+
              str(parsed_json['history']['dailysummary'][0]['date']['year']))


print(datePulled)


def query_API(self):
    state = self.state
    city = self.city
    queryString = 'http://api.wunderground.com/api/f3cdf122d8571d47/forecast10day/q/'+state+'/'+city+'.json'
    tenDay=urllib2.urlopen(queryString)
    queryString = 'http://api.wunderground.com/api/Your_Key/yesterday/q/'+state+'/'+city+'.json'
    yesterday = urllib2.urlopen(queryString)
    return(tenDay,yesterday);
		
def getJSONData(self):
    tenDayYesterday = self.query_API()
    tenDay = tenDayYesterday[0]
    yesterday = tenDayYesterday[1]
    
    state = self.state
    city = self.city
    #f = urllib2.urlopen('http://api.wunderground.com/api/f3cdf122d8571d47/forecast10day/q/CO/Boulder.json')
    json_string = tenDay.read()
    parsed_json = json.loads(json_string)
    highList= []
    lowList = []
    name = city+state
