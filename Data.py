#import RPi.GPIO as GPIO

class Data:
    waterSensors = [1,2,3] # array holding pin numbers for water sensors
    ecSensors = [4,5,6] # same thing

    def __init__(self):
        #GPIO.setmode(GPIO.BOARD)

        for i in self.waterSensors:
            #GPIO.setup(i, GPIO.in)
            print("setting up")

        for i in self.ecSensors:
            # GPIO.setup(i, GPIO.in)
            print("setting up")

        #GPIO.setup(switch, GPIO.IN)


    def __getWaterSensor__(pin):
        #return GPIO.input(waterSensor[pin])
        print("returning value")

    def __getECSensor__(pin):
        # return GPIO.input(ecSensors[pin])
        print("returning value")

