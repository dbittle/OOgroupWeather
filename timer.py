import time 

class timer:

	__observers = []
	 
	def _init_(self):
		pass
		
	def attach(observer):
		observers.append(observer)
		
	def __update(self):
		for o in self.__observers:
			o.update('newDay')
	
	def monitorDate(self):
		#currentDate = (time.strftime("%d/%m/%Y"))
		#print 'going to sleep soon test'

		while(1):
			self.__update()
			time.sleep(86400) 
		
t = timer()
#t.monitorDate()

		
		

