#! /usr/bin/python
# python program to communicate with an MCP3008. 
# Base Code written by seempie from instructables.com

# Import SpiDev wrapper and our sleep function
import spidev
from time import sleep

# Establish SPI device on Bus 0,Device 0
spi = spidev.SpiDev()
spi.open(0,0)

def getAdc(channel):
    #check valid channel
    if ((channel>7)or(channel<0)):
        return -1
        
    while True:
        # Perform SPI transaction and store returned bits in 'r'
        r = spi.xfer([1, (8+channel) << 4, 0])
        
        #Filter data bits from retruned bits
        adcOut = ((r[1]&3) << 8) + r[2]
        percent = int(round(adcOut/10.24))
        
        #print out 0-1023 value and percentage
        print "ADC Output: {0:4d} Percentage: {1:3}%".format (adcOut,percent)
        sleep(10)

if __name__ == '__main__':
    getAdc(0)