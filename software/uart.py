#!/usr/bin/env python


import time
import serial
import RPi.GPIO as GPIO
import os
import threading




class uartThread(threading.Thread):
    def __init__(self, display):
        threading.Thread.__init__(self)
	self.display = display
        self.valid_run = True

        self.ser = serial.Serial(
               port='/dev/ttyS0',
               baudrate = 9600,
               parity=serial.PARITY_NONE,
               stopbits=serial.STOPBITS_ONE,
               bytesize=serial.EIGHTBITS,
               timeout=1
           )

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18,GPIO.IN)
        self.ser.flushInput()

    def run(self):
        Buff=['1','2','3','4','5','6']

        while self.valid_run:
            if(GPIO.wait_for_edge(18, GPIO.RISING, timeout=5000)):
                if self.ser.read()=="A":
                    for i in range(6):
                        Buff[i]=self.ser.read()
                    print(Buff)
                    x='A'
                    x=ord(x)
                    for i in range(5):
                        x=x^ord(Buff[i])
                    if x==ord(Buff[5]):
                        print("\nCRC OK\n")
                        pisen=int(Buff[0])*100+int(Buff[1])*10+int(Buff[2])
                        sloka=int(Buff[3])*10+int(Buff[4])
                        self.display.set_number("%05d" % (pisen * 100 + sloka) )
                        #s='Pisen je ' + repr(Pisen) + ' Sloka je ' + repr(Sloka)
                        #print(s)

                    else:
                        print "CRC fail"

    def stop(self):
        self.valid_run = False



