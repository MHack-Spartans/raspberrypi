import RPi.GPIO as GPIO
import time

RedPin = 22
GreenPin = 23
BluePin = 27

GPIO.setmode(GPIO.BOARD)
GPIO.setup(RedPin, GPIO.OUT)
GPIO.setup(GreenPin, GPIO.OUT)
GPIO.setup(BluePin, GPIO.OUT)

GPIO.output(RedPin, GPIO.HIGH)
GPIO.output(Green
Pin, GPIO.HIGH)
GPIO.output(BluePin, GPIO.HIGH)
