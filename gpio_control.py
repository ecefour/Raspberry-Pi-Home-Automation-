#Created by Sam Errett 
#Updated March 19, 2018

#!/usr/bin/python
from flask import Flask
from flask_ask import Ask, statement, convert_errors
import RPi.GPIO as GPIO
import logging
import sys
import Adafruit_DHT
import time
import threading
import random
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

app = Flask(__name__)
ask = Ask(app, '/')

#RED = 25
#GREEN = 24
#BLUE = 23

GPIO.setup(13,GPIO.OUT)
pwm=GPIO.PWM(13,50)
pwm.start(5)

os.system("gpio -g mode 18 pwm")
os.system("gpio pwm-ms")
os.system("gpio pwmc 192")
os.system("gpio pwmr 2000")
os.system("gpio -g pwm 18 85")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

GPIO.setup(19,GPIO.OUT)
GPIO.output(19,GPIO.HIGH)

@ask.intent('GPIOControlIntent', mapping={'status': 'status'})
def gpio_status(status):

    if status in ['1 on']:
      os.system("gpio -g mode 18 pwm")
      os.system("gpio pwm-ms")
      os.system("gpio pwmc 192")
      os.system("gpio pwmr 2000")
      os.system("gpio -g pwm 18 200")
      return statement('turning light one on')

    if status in ['2 on']:
      pwm.ChangeDutyCycle(7.5)
      return statement('turning light two on')

    if status in ['2 off']:
      pwm.ChangeDutyCycle(3)
      return statement('turning light two off')

    if status in ['on the lamp' ]:
      GPIO.setup(21, GPIO.IN)
      state = GPIO.input(21)
      if (state == True):
        GPIO.setup(21, GPIO.OUT)
        GPIO.output(21,GPIO.LOW)
        return statement('turning on the lamp')
      else:
        GPIO.setup(21, GPIO.OUT)
        GPIO.output(21,GPIO.LOW)
        return statement('lamp already off')

    if status in ['white']:
      GPIO.setup(24, GPIO.OUT)
      GPIO.setup(23, GPIO.OUT)
      GPIO.setup(25, GPIO.OUT)
      GPIO.output(24,GPIO.HIGH)
      GPIO.output(25,GPIO.HIGH)
      GPIO.output(23,GPIO.HIGH)
      return statement('turning light white')

    if status in ['yellow']:
      GPIO.setup(24, GPIO.OUT)
      GPIO.setup(23, GPIO.OUT)
      GPIO.setup(25, GPIO.OUT)
      GPIO.output(24,GPIO.HIGH)
      GPIO.output(25,GPIO.HIGH)
      GPIO.output(23,GPIO.LOW)
      return statement('turning light yellow')

    if status in ['color light', 'rgb']:
      GPIO.setup(24, GPIO.OUT)
      GPIO.setup(23, GPIO.OUT)
      GPIO.setup(25, GPIO.OUT)
      GPIO.output(24,GPIO.LOW)
      GPIO.output(25,GPIO.LOW)
      GPIO.output(23,GPIO.LOW)
      return statement('turning {} Off'.format(status))

    if status in ['r.g.b.', 'r. g. b.']:
      GPIO.setup(24, GPIO.OUT)
      GPIO.setup(23, GPIO.OUT)
      GPIO.setup(25, GPIO.OUT)
      GPIO.output(24,GPIO.LOW)
      GPIO.output(25,GPIO.LOW)
      GPIO.output(23,GPIO.LOW)
      return statement('turning {} Off'.format(status))

    if status in ['blue']:
      GPIO.setup(23, GPIO.IN)
      state = GPIO.input(23)
      GPIO.setup(24, GPIO.OUT)
      GPIO.setup(23, GPIO.OUT)
      GPIO.setup(25, GPIO.OUT)
      GPIO.output(24,GPIO.LOW)
      GPIO.output(25,GPIO.LOW)
      GPIO.output(23,GPIO.HIGH)
      return statement('turning light blue')

    if status in ['rgv', 'r.g.b']:
      GPIO.setup(24, GPIO.OUT)
      GPIO.setup(23, GPIO.OUT)
      GPIO.setup(25, GPIO.OUT)
      GPIO.output(24,GPIO.LOW)
      GPIO.output(25,GPIO.LOW)
      GPIO.output(23,GPIO.LOW)
      return statement('turning rgb off'.format(status))

    if status in ['colored light', 'the color light']:
      GPIO.setup(24, GPIO.OUT)
      GPIO.setup(23, GPIO.OUT)
      GPIO.setup(25, GPIO.OUT)
      GPIO.output(24,GPIO.LOW)
      GPIO.output(25,GPIO.LOW)
      GPIO.output(23,GPIO.LOW)
      return statement('turning rgb off'.format(status))

    if status in ['purple']:
      GPIO.setup(24, GPIO.OUT)
      GPIO.setup(23, GPIO.OUT)
      GPIO.setup(25, GPIO.OUT)
      GPIO.output(24,GPIO.LOW)
      GPIO.output(25,GPIO.HIGH)
      GPIO.output(23,GPIO.HIGH)
      return statement('turning light purple')

    if status in ['1 off']:
      os.system("gpio -g mode 18 pwm")
      os.system("gpio pwm-ms")
      os.system("gpio pwmc 192")
      os.system("gpio pwmr 2000")
      os.system("gpio -g pwm 18 100")
      return statement('turning light one on')

    if status in ['light blue']:
      GPIO.setup(24, GPIO.OUT)
      GPIO.setup(23, GPIO.OUT)
      GPIO.setup(25, GPIO.OUT)
      GPIO.output(24,GPIO.HIGH)
      GPIO.output(25,GPIO.LOW)
      GPIO.output(23,GPIO.HIGH)
      return statement('turning light, light blue')

    if status in ['red']:
      GPIO.setup(24, GPIO.OUT)
      GPIO.setup(23, GPIO.OUT)
      GPIO.setup(25, GPIO.OUT)
      GPIO.output(24,GPIO.LOW)
      GPIO.output(25,GPIO.HIGH)
      GPIO.output(23,GPIO.LOW)
      return statement('turning light red')

    if status in ['green']:
      GPIO.setup(24, GPIO.OUT)
      GPIO.setup(23, GPIO.OUT)
      GPIO.setup(25, GPIO.OUT)
      GPIO.output(24,GPIO.HIGH) 
      GPIO.output(25,GPIO.LOW)
      GPIO.output(23,GPIO.LOW)
      return statement('turning light green')

    if status in ['off the lamp','off my lamp' ]:
      GPIO.setup(21, GPIO.OUT)
      GPIO.output(21,GPIO.HIGH)
      return statement('Turning {}'.format(status))

    if status in ['cancel', 'stop']:
      GPIO.setup(20, GPIO.IN)
      state = GPIO.input(20)
      if (state == True):
        GPIO.setup(20, GPIO.OUT)
        GPIO.output(20,GPIO.HIGH)
        return statement('your drink has been canceled')
      else:
        GPIO.setup(20, GPIO.OUT)
        GPIO.output(20,GPIO.HIGH)
        return statement('no drink is being made')

    if status in ['done', 'finished']:
      GPIO.setup(20, GPIO.IN)
      state = GPIO.input(20)
      GPIO.setup(20, GPIO.OUT)
      GPIO.output(20,GPIO.HIGH)
      return statement('your drink is {}'.format(status))

    if status in ['coffee', 'tea']:
      GPIO.setup(20, GPIO.IN)
      state = GPIO.input(20)
      if (state == True):
        GPIO.setup(20, GPIO.OUT)
        GPIO.output(20,GPIO.LOW)
        return statement('your {} will be completed in approximately 4 to 12 minutes'.format(status))
      else:
        GPIO.setup(20, GPIO.OUT)
        GPIO.output(20,GPIO.LOW)
        return statement('making {}'.format(status)) 

    if status in ['temperature', 'temp']:
      humidity, temperature = Adafruit_DHT.read_retry(11, 4)
      return statement('the temperature is currently {} degrees celsius'.format(temperature))

    if status in ['humidity', 'humid']:
      humidity, temperature = Adafruit_DHT.read_retry(11, 4)
      return statement('the humidity  is currently {} %'.format(temperature))

if __name__ == '__main__':
  port = 5000 #ngrok port
  app.run(host='0.0.0.0', port=port)

if KeyboardInterrupt:
  print "You've exited the program"
  os.system("gpio -g mode 18 pwm")
  os.system("gpio pwm-ms")
  os.system("gpio pwmc 192")
  os.system("gpio pwmr 2000")
  os.system("gpio -g pwm 18 85")
  GPIO.cleanup()
