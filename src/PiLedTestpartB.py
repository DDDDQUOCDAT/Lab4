import hal
import time
from hal import hal_led as led
from hal import hal_input_switch as slide
def Led_blink(delay):
    slide.init()
    led.init()
    while slide.read_slide_switch()==1:
        led.set_output(24, 1)
        time.sleep(delay)

        led.set_output(24, 0)
        time.sleep(delay)

        led.set_output(24, 1)
        time.sleep(delay)

        led.set_output(24, 0)
        time.sleep(delay)

if __name__== "__main__":
    while True:
        Led_blink(0.2)