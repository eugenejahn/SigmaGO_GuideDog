# Import required Python libraries
# -----------------------
import time
import RPi.GPIO as GPIO

# -----------------------
# Define some functions
# -----------------------
class ult():
    def __init__(self):
        
        GPIO.setmode(GPIO.BOARD)
        self.GPIO_TRIGGER = 36
        self.GPIO_ECHO    = 37
        GPIO.setup(self.GPIO_TRIGGER,GPIO.OUT)
        GPIO.setup(self.GPIO_ECHO,GPIO.IN)
        GPIO.output(self.GPIO_TRIGGER,False)

    def measure(self):
        # This function measures a distance
        #GPIO.setmode(GPIO.BOARD)
        try:
            GPIO.output(self.GPIO_TRIGGER, GPIO.HIGH)
            time.sleep(0.00001)
            GPIO.output(self.GPIO_TRIGGER, GPIO.LOW)
            start = time.time()

            while GPIO.input(self.GPIO_ECHO)==0:
                start = time.time()
                #print(0)
            while GPIO.input(self.GPIO_ECHO)==1:
                stop = time.time()
                #print(1)
            elapsed = stop - start
            distance = (elapsed * 34300)/2
            #print(distance)
            return distance
        except (KeyboardInterrupt, SystemExit):
            self.quit()
              
    def measure_average(self):
    # This function takes 3 measurements and
    # returns the average.
        try:
            distance1=self.measure()
            time.sleep(0.025)
            distance2=self.measure()
            time.sleep(0.025)
            distance3=self.measure()
            distance = distance1 + distance2 + distance3
            distance = distance / 3
            #print(distance)
            return distance
        except( KeyboardInterrupt, SystemExit):
            self.quit()
    def quit(self):
        GPIO.cleanup()
