import RPi.GPIO as GPIO
from time import sleep
import subprocess

# Varibles (degree: percentage)
degrees = {35: 20, 45: 40, 55: 50, 70: 100}
fan_pin = 12
min_temp = 34

# GPIO Config
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(fan_pin, GPIO.OUT)
fan_pwm = GPIO.PWM(fan_pin, 100)
fan_pwm.start(0)


while True:
    cur_temp = int(float(subprocess.check_output(["cat /sys/class/thermal/thermal_zone0/temp"], shell=True).decode().strip()) / 1000)

    if cur_temp > min_temp:
        last_speed = degrees.get(cur_temp) or degrees[min(degrees.keys(), key = lambda key: abs(key-cur_temp))]
    else:
        last_speed = 0

    fan_pwm.ChangeDutyCycle(last_speed)
    print("Temperature: {}°C, Fan Speed: {}%".format(cur_temp, last_speed))

    sleep(10)


fan_pwm.stop()
GPIO.cleanup()
