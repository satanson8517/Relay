#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(15, GPIO.OUT)

while True:
    GPIO.output(15, True)
    time.sleep(1)
    GPIO.output(15, False)
    time.sleep(1)

