'''
Created on Jun 28, 2017

@author: make ma
'''
from AudioSrc import AudioSrc
from MsgHandler import MsgConst, MsgHandler
from OlamiNlp import OlamiNlp
from VoiceCmd import VoiceCmd
from threading import Thread
from Config import Config
import time
import Googleapi_test
import GPS_test
import move_car
import readchar
import ult_lib
import re
import joystick_lib
#import gpsGoogle
from gps3.agps3threaded import AGPS3mechanism
  
class ult_detect(Thread):
    def __init__(self):
        Thread.__init__(self)
    def init(self,handler):
        self.ult = ult_lib.ult()
        self.audioSrc = AudioSrc() 
        self.handler = handler
        self.start()
        #self.lock  = Lock()
        self.move = move_car.carMove()

    #def lock(self):

    def run(self):
        #try:
        while(True):
            #self.handler.sendEmptyMessage(MsgConst.MSG_FORCE_STOP_TTS)
            if self.ult.measure_average() <= 20:
                print("close")
                print(self.ult.measure_average()) 
                msg = self.handler.obtainMessage1(MsgConst.MSG_NORMAL_TTS_PLAY)
                msg.obj = "太近了"
                self.handler.sendMessage(msg)
                time.sleep(0.3)
                self.audioSrc.clearData()  
                self.move.stop()
            time.sleep(1)
        #except (KeyboardInterrupt, SystemExit):
            #self.ult.quit()



        #SpeechProcess.ult_sensor(self)
class SpeechProcess(Thread):
    '''
    classdocs
    '''
    def __init__(self):
        Thread.__init__(self, name = "SpeechProcess")
        
        
    def init(self, handler):
        
        self.handler = handler  
        self.audioSrc = AudioSrc()        
        self.audioSrc.startRecord()  
        self.voiceCmd = VoiceCmd()
        self.voiceCmd.init(self.audioSrc)
        self.setDaemon(True)
        self.nlp = OlamiNlp()
        self.nlp.setLocalization(Config.NLI_SERVER)
        self.nlp.setAuthorization(Config.APP_KEY, Config.APP_SECRET)     
        #self.gps = gpsGoogle.gps()

        self.joystick = joystick_lib.joystick()
        self.joystick.start()

        self.agps_thread = AGPS3mechanism()
        self.agps_thread.stream_data()
        self.agps_thread.run_thread()

        self.ultThread = ult_detect()
        #self.gps.start()
        self.move = move_car.carMove()
        self.start()      
        #self.ultThread.start()
        
        return True
    
    def destroy(self):
        self.needStop = True
        self.join(2000)        
        self.audioSrc.stopRecord()        
        self.voiceCmd.destroy()
        
    def wakeupNow(self):
        self.voiceCmd.cancelDetect()
    def getLatLon(self):
        lat = self.agps_thread.data_stream.lat
        lon = self.agps_thread.data_stream.lon
        print('---------------------')
        #print(                   self.agps_thread.data_stream.time)
        print('Lat:{}   '.format(lat))
        print('Lon:{}   '.format(lon))
        #print('Speed:{} '.format(self.agps_thread.data_stream.speed))
        #print('Course:{}'.format(self.agps_thread.data_stream.track))
        print('---------------------')
        return (str(lat),str(lon) )

    def directionMove(self, direction):
        #tmp = (((len(direction)-2)/3)*2 + 1)
        tmp = (((len(direction)-2)/3) +1)
        print(tmp)
        tmp = int(tmp)
        newDirection = [0]*tmp
        for i in range(tmp):
            if i == 0:
                newDirection[0] = direction[0] + direction[1]
            #elif ( i%2 == 0):
                #newDirection[i] = direction[int((i/2)*3)]+ direction[int((i/2)*3+1)]
            else:
                #newDirection[i] = direction[int(((i-1)/2)*3+2)]
                newDirection[i] = direction[(i*3)-1] + ' ' +  direction[(i*3)] + ' '+  direction[(i*3)+1] 
        print(newDirection)

        for d in newDirection:
            msg = self.handler.obtainMessage1(MsgConst.MSG_NORMAL_TTS_PLAY)
            msg.obj = d
            self.handler.sendMessage(msg)
            time.sleep(len(d)*0.3)
            self.audioSrc.clearData()
            words = d.split()
            print(words)
            for dd in words:
                print( dd)
                if dd == '前進':
                    movetime = int(re.search(r'\d+', words[-2]) .group())*10
                    print(movetime)
                    self.move.forward(movetime)
                    print('Go')
                elif dd == '左':
                    movetime = int(re.search(r'\d+', words[-2]) .group())*10
                    self.move.turnLeft(movetime)
                    print('Left')
                elif dd == '右':
                    movetime = int(re.search(r'\d+', words[-2]) .group())*10
                    self.move.turnLeft(movetime)
                    print('Right')
            time.sleep(10)

    def run(self):
        self.needStop = False        
        Direction = Googleapi_test.Googleapi_test()
        gps_test = GPS_test.GPS_test()
        #move = move_car.carMove()
       
       
        try:
            while not self.needStop:
                #self.getLatLon()               
                wakeup = self.voiceCmd.startDetect()
                self.handler.sendEmptyMessage(MsgConst.MSG_FORCE_STOP_TTS)
              
                #move.forward()
                #print(0)
                #self.ult_sensor()
                #if ult.measure_average() <= 17:
                    #print("close")
                    #msg = self.handler.obtainMessage1(MsgConst.MSG_NORMAL_TTS_PLAY)
              #msg.obj = "太近了"
                    #self.handler.sendMessage(msg)
                    #time.sleep(0.5)
                    #self.audioSrc.clearData() 
               
                if wakeup != VoiceCmd.STATE_STOPPED:  
                        
                    if wakeup == VoiceCmd.STATE_DETECTED_KEY:
                        msg = self.handler.obtainMessage1(MsgConst.MSG_NORMAL_TTS_PLAY)
                        msg.obj = "在"                
                        self.handler.sendMessage(msg)
                        time.sleep(0.5)
                        #self.audioSrc.clearData() 
                        #gps_test.GPS_Speech()
                        self.audioSrc.clearData()
                    #self.ultThread.pause()
                    #print('start')
                    nlpResult = self.nlp.getNlpResult(self.audioSrc)
                    #self.ultThread.resume()
                    #print(0)
                    print (nlpResult)
                    if nlpResult != None:
                        #print(0)
                        if nlpResult [0]['type'] == 'google_test':
                            lat , lon = self.getLatLon()
                            print(lat + '\n')
                            print(lon + '\n')
                            destination = nlpResult[0]['semantic'][0]['slots'][0]['value']
                            direction = Direction.googleapi(destination.encode('big5'), lat, lon)
                            direction = direction.splitlines()
                            print (direction) 
                            self.directionMove(direction)
                            #nlpResult[0]['desc_obj']['result'] = direction
                            print (direction)
                        elif nlpResult [0]['type'] == 'guide_dog':
                            data = nlpResult[0]['semantic'][0]['modifier']
                            print (data)
                            if data == ['go_toward']:
                                #print('Got go_toward')
                                self.move.forward(5)
                            elif data == ['go_backward']:
                                self.move.backward()
                            elif data == ['go_right']:
                                self.move.turnRight(5)
                            elif data == ['go_left']:
                                self.move.turnLeft(5)
                            elif data == ['stop']:
                                self.move.stop()
                        #print (1)
                        msg = self.handler.obtainMessage1(MsgConst.MSG_DATA_FROM_SERVER)
                        msg.obj = nlpResult
                        print(0)
                        #self.ultThread.pause()  
                        print(1)
                        self.handler.sendMessage(msg)
                        #self.ultThread.resume() 
                    self.audioSrc.clearData()
        except (KeyboardInterrupt, SystemExit):
            self.move.quit()
              
                
                
        
        
