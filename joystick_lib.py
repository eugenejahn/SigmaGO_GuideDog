import spidev
import time
import os
import move_car
from threading import Thread
#import joystick_lib
class joystick(Thread):
    def __init__(self):
# open SPI bus
        Thread.__init__(self)
        self.spi = spidev.SpiDev()
        self.spi.open(0,0)
    def init(self):
        #self.spi = spidev.SpiDev()
        #self.spi.open(0,0)
        self.start()

# read SPI data from  MCP3008 , Channel must be 0-7
    def ReadChannel(self, channel):
        adc = self.spi.xfer2([1,(8+channel)<<4,0])
        data = ((adc[1]&3) << 8) + adc[2]
        return (data)

      # Define sensor channels
    def run(self):
        sw_ch = 0
        vx_ch = 1
        vy_ch = 2

        # Define delay between readings
        delay = 0.01
        move = move_car.carMove()
        movetime = 0.5
        while True:

            # Read the joystick position data
            vx_pos = self.ReadChannel(vx_ch)
            vy_pos = self.ReadChannel(vy_ch)

            # Read switch state
            sw_val = self.ReadChannel(sw_ch)

            if int(vx_pos) >= 800:
                # print( "UP...")
                move.forward(movetime)
            if int(vx_pos) <= 100:
                #print( "Down...")
                move.backward()

            if int(vy_pos) <= 300:
                # print ("Left...")
                move.turnLeft(movetime)
            if int(vy_pos) >= 800:
                # print ("Right...")
                move.turnRight(movetime)
            #if int(sw_val) >= 1023:
                #                print ("Press...")
                #move.stop()
    # Wait time
            time.sleep(delay)

#joystick = joystick_lib.joystick()
#joystick.start()
