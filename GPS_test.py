from MsgHandler import MsgConst, MsgHandler
import time 

class GPS_test():
    def GPS_test(self):
        '''
        hihihih
        '''
    def GPS_Speech(self):

        msgConst   = MsgConst()
        msgHandler = MsgHandler()
        msgHandler.sendEmptyMessage(msgConst.MSG_FORCE_STOP_TTS)
        msg = msgHandler.obtainMessage1(msgConst.MSG_NORMAL_TTS_PLAY)

        print('hihihihihhhihihihihihihihihihhh')
        msg.obj = "有何"
        msgHandler.sendMessage(msg)
        time.sleep(0.5)





