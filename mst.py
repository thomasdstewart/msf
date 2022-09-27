#!/usr/bin/env python3
import RPi.GPIO as GPIO
import datetime
import time
from pprint import pprint as pp

pin = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)

last = -1
while True:
    reading = GPIO.input(pin)
    if(reading != last):
        last = reading
        print("%s %s" % (datetime.datetime.now(), reading))

#    time.sleep(0.1)

#https://www.bigmessowires.com/2018/05/26/raspberry-pi-gpio-programming-in-c/
#https://www.mas-oy.com/wp-content/uploads/2016/05/DAEV6180B1COB.pdf
#https://github.com/benclifford/msf/blob/master/shift.c
