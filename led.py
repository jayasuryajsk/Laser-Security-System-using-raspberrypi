from os import system
from gpiozero import LED, LightSensor
from time import sleep
import opto
import sms

ldr = LightSensor(4)
led = LED(17)

while True:
        if ldr.value < 0.2:
                print(ldr.value)
                led.on()
                sms.send_sms()
                opto.send_mail()
                

        else:
                print(ldr.value)
                led.off()
