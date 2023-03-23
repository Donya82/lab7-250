import RPi.GPIO as GPIO
import time

def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)

    while True:
        # Test 1: blink LED 5 times w on/off intervals 500ms
        for i in range(5):
            GPIO.output(11, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(11, GPIO.LOW)
            time.sleep(0.5)

        # Test 2:For about 5 seconds, read the output of the Grove light sensor with intervals of
#100 ms and print the raw value along with the text “bright” or “dark” (you will have
#to determine a threshold for this through experimentation).


        # Test 3: Blink the LED 4 times with on/off intervals of 200ms.
        for i in range(4):
            GPIO.output(11, GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(11, GPIO.LOW)
            time.sleep(0.2)


        # Test 4: For about 5 seconds, read the output of the Grove sound sensor with intervals of
#100 ms and print the raw value. If the sound sensor is tapped (i.e. the sound
#magnitude goes above the threshold you decide from experimentation), the LED
#should turn on for 100 ms.
            

if __name__ == "__main__":
    main()
