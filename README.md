# AG-TECH-RASBERRYPI

Ag tech Arduino code for sending data
Rasberry-Pi stuff
	
	Data:
		Two water level sensors
		4 EC sensors
		some other stuff I cant remember	

	Language- Perferably java or python, it needs to connect to sql and the GPIO pins so make it easy
	
	Main Class-
		Periodically take the data readings from the sensors. 
		Upload data to SQL database
		Store data every few minutes and calulcate average of each
		
		
	Sensors Class-
		-getWaterSensors(){
			readPort whatever
		}
		-getData() return current data
		
	SQL Class-
		-uploadData(averaged values){
			convert to DB format and upload
		}
			
