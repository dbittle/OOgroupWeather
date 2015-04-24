import time 
from Wunderground_pull import Wunderground_pull

class timer:

	listofCities = [("New_York",'NY'),("Los_Angeles","CA"),("Ardmore","PA"),("Honolulu","HI"),("Boulder","CO"),("Aurora","CO")]
	listofobservers = []
	def _init_(self):
		pass
		
	def attach(self, observer):
		self.listofobservers.append(observer)
		
	def Notify(self):
		for o in self.listofobservers:
			o.update(self.listofCities)
	
	def monitorDate(self):
		#currentDate = (time.strftime("%d/%m/%Y"))
		#print 'going to sleep soon test'

		while(1):
			#self.__update()
			#time.sleep(86400)
			self.Notify()
			time.sleep(86400/2)
			
			
t = timer()
observer1 = Wunderground_pull("Wunderground")
t.attach(observer1)
t.monitorDate()
		

