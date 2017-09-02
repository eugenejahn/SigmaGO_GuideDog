#!/usr/bin/python 

import RPi.GPIO as GPIO
import time
import readchar

class carMove():
    def __init__(self):
        self.Motor_R1_Pin = 18
        self.Motor_R2_Pin = 16
        self.Motor_L1_Pin = 11
        self.Motor_L2_Pin = 13
        self.t = 1

       # GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.Motor_R1_Pin, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.Motor_R2_Pin, GPIO.OUT, initial=GPIO.LOW) 
        GPIO.setup(self.Motor_L1_Pin, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.Motor_L2_Pin, GPIO.OUT, initial=GPIO.LOW)
         
    def stop(self):
        
        GPIO.output(self.Motor_R1_Pin, False)
        GPIO.output(self.Motor_R2_Pin, False)
        GPIO.output(self.Motor_L1_Pin, False)
        GPIO.output(self.Motor_L2_Pin, False)
       

    def forward(self,t):
        
        GPIO.output(self.Motor_R1_Pin, True)
        GPIO.output(self.Motor_R2_Pin, False)
        GPIO.output(self.Motor_L1_Pin, True)
        GPIO.output(self.Motor_L2_Pin, False)
        time.sleep(t)
        print('hihihhihhhihhhihiiiihihihihihihhihihihihihihihihih')
        self.stop()
        


    def backward(self):
        GPIO.output(self.Motor_R1_Pin, False)
        GPIO.output(self.Motor_R2_Pin, True)
        GPIO.output(self.Motor_L1_Pin, False)
        GPIO.output(self.Motor_L2_Pin, True)
        time.sleep(self.t)
        self.stop()
        


    def turnRight(self,t):
        GPIO.output(self.Motor_R1_Pin, True)
        GPIO.output(self.Motor_R2_Pin, False)
        GPIO.output(self.Motor_L1_Pin, False)
        GPIO.output(self.Motor_L2_Pin, False)
        time.sleep(t)
        self.stop()
       

    def turnLeft(self,t):
        
        GPIO.output(self.Motor_R1_Pin, False)
        GPIO.output(self.Motor_R2_Pin, False)
        GPIO.output(self.Motor_L1_Pin, True)
        GPIO.output(self.Motor_L2_Pin, False)
        time.sleep(t)
        self.stop()
        
    def quit(self):
        GPIO.cleanup()



