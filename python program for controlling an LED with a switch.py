from time import sleep
import RPI.GPio as GPIO

GPIO.setmode(GPIO.BCM)

#Switch Pin
GPIO.setup(25, GPIO.IN)

#LED Pin
GPIO.setup(18, GPIO.OUT)

state=false

def toggleLED(pin):
  state = not state
  GPIO.output(pin,state)

while True:
  try:
    if (GPIO.input (25) == True):
      toggleLED(pin)
      sleep(0.1)

except KeybpardINterrput:
exit()

