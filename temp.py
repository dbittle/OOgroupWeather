listofCities = (("New_York",'NY'),("Los_Angeles","CA"),("Ardmore","PA"),("Honolulu","HI"),("Boulder","CO"),("Aurora","CO"))
print(listofCities[0][0])
print(len(listofCities))

for x in range(0,(len(listofCities))):
    #Wunderground_pull('Wunderground','Honolulu','HI')
    Wunderground_pull('Wunderground',listofCities[x][0],listofCities[x][1])
    #print(listofCities[x][0])
