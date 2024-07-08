import hal
import time
from hal import hal_led as led
from hal import hal_input_switch as slide
def main():
    slide.init()
    led.init()
    while slide.read_slide_switch()==1:
        blink(0.2)
    while slide.read_slide_switch()==0:
        blink(0.1)

def blink(delay):
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
        main()