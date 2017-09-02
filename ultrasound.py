# Import required Python libraries
# -----------------------
import time
import RPi.GPIO as GPIO

# -----------------------
# Define some functions
# -----------------------

def measure():
      # This function measures a distance

    GPIO.output(GPIO_TRIGGER, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, GPIO.LOW)
    start = time.time()

    while GPIO.input(GPIO_ECHO)==0:
        start = time.time()
        #print(0)
    while GPIO.input(GPIO_ECHO)==1:
        stop = time.time()
        #print(1)
    elapsed = stop - start
    distance = (elapsed * 34300)/2
    print(distance)
    return distance

def measure_average():
# This function takes 3 measurements and
# returns the average.

    distance1=measure()
    time.sleep(0.1)
    distance2=measure()
    time.sleep(0.1)
    distance3=measure()
    distance = distance1 + distance2 + distance3
    distance = distance / 3
    print(distance)
    return distance

# -----------------------
# Main Script
# -----------------------

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BOARD)

# Define GPIO to use on Pi
GPIO_TRIGGER = 36
GPIO_ECHO    = 37

print "Ultrasonic Measurement"

# Set pins as output and input
GPIO.setup(GPIO_TRIGGER,GPIO.OUT,initial = GPIO.LOW)  # Trigger
GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo

# Set trigger to False (Low)
GPIO.output(GPIO_TRIGGER, False)

try:

    while True:
        print('hi')
        distance = measure_average()
        print "Distance : %.1f" % distance
        time.sleep(1)

except KeyboardInterrupt:
# User pressed CTRL-C
# Reset GPIO settings
    GPIO.cleanup()
