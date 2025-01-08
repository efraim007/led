#Complete Project Details: https://RandomNerdTutorials.com/raspberry-pi-pwm-python/

from gpiozero import PWMLED
from time import sleep

ledb = PWMLED(16)
ledz = PWMLED(20)
ledr = PWMLED(21)

nino =1
while nino < 4:
    ledr.value = 1
    ledb.value = 0 
    sleep(0.5)
    ledr.value = 0
    ledb.value = 1 
    sleep(0.5)
    nino+=1
ledb.value=0
ledr.value=0
sleep(2)
try:
  # fade in and out forever
  while True:
    # red fade in > out
    for duty_cycle in range(0, 100, 1):
      ledr.value = duty_cycle/100.0
      sleep(0.05)  
    for duty_cycle in range(100, 0, -1):
      ledr.value = duty_cycle/100.0
      sleep(0.05)
    # blue fade in > out
    for duty_cycle in range(0, 100, 1):
      ledr.value =0
      ledb.value = duty_cycle/100.0
      sleep(0.05)
    for duty_cycle in range(100, 0, -1):
      ledb.value = duty_cycle/100.0
      sleep(0.05)
      
except KeyboardInterrupt:
  print("Stop the program and turning off the LED")
  ledr.value = 0
  pass