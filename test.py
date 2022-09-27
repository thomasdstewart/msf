#!/usr/bin/env python3
import time
import RPi.GPIO as GPIO
from pprint import pprint as pp

#GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
#GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while(True):
    print("%s" % GPIO.input(12))
    time.sleep(0.05)
