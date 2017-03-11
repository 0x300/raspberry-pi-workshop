import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

pins = [36,38,40]

GPIO.setup(pins, GPIO.OUT, initial = GPIO.LOW)

while True:
    GPIO.output(pins[0], GPIO.HIGH)
    GPIO.output(pins[1], GPIO.HIGH)
    GPIO.output(pins[2], GPIO.HIGH)

    time.sleep(0.25)

    GPIO.output(pins[0], GPIO.LOW)
    GPIO.output(pins[1], GPIO.LOW)
    GPIO.output(pins[2], GPIO.LOW)

    time.sleep(0.25)
