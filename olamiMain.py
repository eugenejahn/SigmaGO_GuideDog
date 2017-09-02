#-*- coding：utf-8 -*-
'''
Created on Jun 27, 2017

@author: make ma
'''

from Config import Config
from ControlCenter import ControlCenter
import readchar
from SpeechProcess import ult_detect
#import move_car
#import RPi.GPIO as GPIO
import move_car

def checkConfig():
    ret = False
    if len(Config.NLI_SERVER) > 0 and len(Config.APP_KEY) > 0 and len(Config.APP_SECRET) > 0:
        ret = True
    else:
        print("Please set NLI_SERVER, APP_KEY, APP_SECRET in Config.py\n")
    return ret

if __name__ == '__main__':
    move = move_car.carMove()
    print("Olami python demo: 1.00\n")
    try:
        if checkConfig():
            controlCenter = ControlCenter()
            ult_detect = ult_detect()
            if controlCenter.init() == True:
                controlCenter.setDaemon(True);
                controlCenter.start()
                #ult_detect.start()
            print("q")
            controlCenter.join()
            controlCenter.uninit()
    except  (KeyboardInterrupt, SystemExit):
        move.quit()

