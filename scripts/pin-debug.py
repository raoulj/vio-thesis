import sys    

import RPi.GPIO as GPIO
import time

set_pin = int(sys.argv[1])
set_power = int(sys.argv[2])

if set_power > 0:
    set_power = GPIO.HIGH
else:
    set_power = GPIO.LOW

GPIO.setmode(GPIO.BCM)
GPIO.setup(set_pin, GPIO.OUT) # output rf

# Initial state for LEDs:
print("Testing RF out, Press CTRL+C or ENTER to exit")

try:
     print("set GIOP high")
     GPIO.output(set_pin, set_power)
     input()               
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
   print("Interupt")
except:
   print("Error") 

finally:
   print("clean up") 
   GPIO.cleanup() # cleanup all GPIO 