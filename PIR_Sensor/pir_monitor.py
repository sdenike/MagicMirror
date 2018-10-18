#!/usr/bin/python
# Import required Python libraries
import RPi.GPIO as GPIO
import subprocess

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_PIR = 7

# Set pin as input
GPIO.setup(GPIO_PIR,GPIO.IN)
Current_State  = 0
Previous_State = 0

try:
  # Loop until PIR output is 0
  while GPIO.input(GPIO_PIR)==1:
    Current_State  = 0
  while True :

    # Read PIR state
    Current_State = GPIO.input(GPIO_PIR)
    if Current_State==1 and Previous_State==0:
      # Exit screensaver if motion is detected
      subprocess.call(['/usr/bin/xscreensaver-command', '-deactivate'])
      # Record previous state
      Previous_State=1
    elif Current_State==0 and Previous_State==1:
      # PIR has returned to ready state
      Previous_State=0

except KeyboardInterrupt:
  # Reset GPIO settings
  GPIO.cleanup()
