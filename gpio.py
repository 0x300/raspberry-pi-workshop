import RPi.GPIO as GPIO
import time

number = 0

GPIO.setmode(GPIO.BOARD)

pins = [35,37,12,16,18,22,32,36,38,40]
GPIO.setup(pins, GPIO.OUT, initial=GPIO.LOW)

while True:
##    number_calc = 0
##
    number += 1
##
##    number_calc = number
##
##    if number_calc >= 8:
##        GPIO.output(32, GPIO.HIGH)
##        number_calc = number - 8
##
##    if number_calc >= 4:
##        GPIO.output(36, GPIO.HIGH)
##        number_calc = number_calc - 4
##
##    if number_calc >= 2:
##        GPIO.output(38, GPIO.HIGH)
##        number_calc = number_calc - 2
##
##    if number_calc >= 1:
##       GPIO.output(40, GPIO.HIGH)

    # Loop over each bit of the current number
    for nth_bit in range(10):
        # Check each of the 4 lowest bits.. if the bit is 1, set LED to HIGH
        if number & (1 << nth_bit):
            GPIO.output(pins[nth_bit], GPIO.HIGH)

##        Else turn it off
        else:
            GPIO.output(pins[nth_bit], GPIO.LOW)

    #time.sleep(0.01)

    #GPIO.output(32, GPIO.LOW)
    #GPIO.output(36, GPIO.LOW)
    #GPIO.output(38, GPIO.LOW)
    #GPIO.output(40, GPIO.LOW)

    #print(number)

    #if number > 14:
    #number = 0

GPIO.cleanup()
