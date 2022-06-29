#!/usr/bin/env python3
#############################################################################
# Filename    : Joystick.py
# Description : Read Joystick state
# Author      : www.freenove.com
# modification: 2020/03/09
########################################################################
import RPi.GPIO as GPIO
import time
from ADCDevice import *

villes = ["Paris", "Marseille", "Lyon", "Dijon", "Nice"]
Z_Pin = 12      # define Z_Pin
adc = ADCDevice() # Define an ADCDevice class object
result = 0

def setup():
    global adc
    if(adc.detectI2C(0x48)): # Detect the pcf8591.
        adc = PCF8591()
    elif(adc.detectI2C(0x4b)): # Detect the ads7830
        adc = ADS7830()
    else:
        print("No correct I2C address found, \n"
        "Please use command 'i2cdetect -y 1' to check the I2C address! \n"
        "Program Exit. \n");
        exit(-1)
    GPIO.setmode(GPIO.BOARD)        
    GPIO.setup(Z_Pin,GPIO.IN,GPIO.PUD_UP)   # set Z_Pin to pull-up mode
def loop():
    i=0
    while True:
        val_Z = GPIO.input(Z_Pin)       # read digital value of axis Z
        val_Y = adc.analogRead(0)           # read analog value of axis X and Y
        val_X = adc.analogRead(1)
        print ('value_X: %d ,\tvlue_Y: %d ,\tvalue_Z: %d'%(val_X,val_Y,val_Z))
        if (val_Z == 0):
            push()
            
        if (val_Y < 120):
            joystickUp()
            if i==0:
                print(i)       
                print (villes[i])
            else:
                i=i-1
                print(i)       
                print (villes[i])
                
        if (val_Y > 135):
            joystickDown()
            if i==len(villes)-1:
                print(i)       
                print (villes[i])
            else:
                i=i+1
                print(i)       
                print (villes[i])
    return i

def destroy():
    adc.close()
    GPIO.cleanup()

def push():
    print('bouton appuyé')
    
def joystickUp():
    print('joystick en haut')
        
def joystickDown():
    print('joystick en bas')
    
if __name__ == '__main__':
    print ('Program is starting ... ') # Program entrance
    setup()
    try:
        loop()
    except KeyboardInterrupt: # Press ctrl-c to end the program.
        destroy()

