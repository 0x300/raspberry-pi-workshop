# Import the General Purpose IO lib so we can control the pins
import RPi.GPIO as GPIO
import time

# Set the mode.. we want to use the physical pin numbers so we choose BOARD
# instead of BCM.. just changes which number refers to which pin later
GPIO.setmode(GPIO.BOARD)

# List of the pins that control the LEDs! :D
pins = [35,37,12,16,18,22,32,36,38,40]

# Initialize the pins.. make them output pins, and we set init state to off
GPIO.setup(pins, GPIO.OUT, initial=GPIO.LOW)

# Now we get to have some fun!!
number_to_display = 0
number_of_leds = 3

while True:
    number_to_display += 1

    # Loop over each bit of the current number
    for nth_bit in range(number_of_leds):
        # Check each of the bits.. if the bit is 1, set LED to HIGH
        if number_to_display & (1 << nth_bit):
            GPIO.output(pins[nth_bit], GPIO.HIGH)

        # Else turn it off
        else:
            GPIO.output(pins[nth_bit], GPIO.LOW)

    # Wait a little bit so we can see the number displayed
    time.sleep(0.1)

GPIO.cleanup()
