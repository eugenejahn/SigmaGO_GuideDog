import spidev
import time
import os
import move_car

# open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)

# read SPI data from  MCP3008 , Channel must be 0-7
def ReadChannel(channel):
    adc = spi.xfer2([1,(8+channel)<<4,0])
    data = ((adc[1]&3) << 8) + adc[2]
    return (data)

      # Define sensor channels
sw_ch = 0
vx_ch = 1
vy_ch = 2

# Define delay between readings
delay = 0.5
move = move_car.carMove()
movetime = 1
while True:

    # Read the joystick position data
    vx_pos = ReadChannel(vx_ch)
    vy_pos = ReadChannel(vy_ch)

    # Read switch state
    sw_val = ReadChannel(sw_ch)

    if int(vx_pos) >= 800:
        print( "UP...")
        move.forward(movetime)
    if int(vx_pos) <= 100:
        print( "Down...")
        move.forward(movetime)

    if int(vy_pos) <= 300:
        print ("Left...")
        move.turnLeft(movetime)
    if int(vy_pos) >= 800:
        print ("Right...")
        move.turnRight(movetime)
    if int(sw_val) >= 1023:
        print ("Press...")
        move.stop()
    # Wait time
    time.sleep(delay)
