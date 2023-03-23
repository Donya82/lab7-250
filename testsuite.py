import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import RPi.GPIO as GPIO
import time

def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)
    SPI_PORT = 0
    SPI_DEVICE = 0
    mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

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

        for i in range(50):
        print(mcp.read_adc(0))
        time.sleep(0.1)
         

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
        for i in range(50):
            print(mcp.read_adc(1))
            time.sleep(0.1)
         

if __name__ == "__main__":
    main()
