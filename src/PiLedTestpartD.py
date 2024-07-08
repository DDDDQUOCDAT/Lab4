import hal
import time
from hal import hal_led as led
from hal import hal_input_switch as slide
def main():
    slide.init()
    led.init()
    end_time = time.time() + 5
    while(True):
        if slide.read_slide_switch()==0:
            while end_time >= time.time():
                print(end_time)
                print(time.time())
                blink(0.1)
                if end_time <= time.time():
                     led.set_output(24, 0)
        if slide.read_slide_switch()==1:
            while slide.read_slide_switch()==1:
                blink(0.2)
                end_time = time.time() + 5

def blink(delay):
    led.set_output(24, 1)
    time.sleep(delay)

    led.set_output(24, 0)
    time.sleep(delay)

if __name__== "__main__":
    main()
