import RPi.GPIO as GPIO
import time
from os import system

# Varibles
button = 40
shutdown_seconds = 3

# GPIO Config
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)


GPIO.wait_for_edge(button, GPIO.FALLING)

print("Button pressed")
start = time.time()
time.sleep(0.2)

while GPIO.input(button) == GPIO.LOW:
    time.sleep(0.01)

signal_length = time.time() - start
print("Signal Length: {}\n".format(signal_length))

if signal_length >= shutdown_seconds:
    system("shutdown -h now")
else:
    system("shutdown -r now")


