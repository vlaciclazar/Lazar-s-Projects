# - - - - - - - - - - - - - - - - - - - - - - - - -
#  Authors: Lazar Vlacic, Emma Vanslack
# 
#  Baby Fever Monitor Code
#
# - - - - - - - - - - - - - - - - - - - - - - - - - 

from gpiozero import LED
import time

blueled = "blue"
greenled = "green"
redled = "red"
yellowled = "yellow"

blueled.off()
greenled.off()
redled.off()
yellowled.off()


def LED_swap(led_off1 , led_off2 , led_off3 , led_on):
    
    led_off1.off()
    led_off2.off()
    led_off3.off()

    led_on.on()
##    print (led_off1 + " is off, " + led_off2 + " is off, " + led_off3 + " is off, " + led_on + " is on")
##    print ("The temperature is " + str(temp) + " degrees")

def LED_flash(led):

    time.sleep(1)

    led.off()
##    print(led + " is off")

    time.sleep(1)
    
   
while True:

##    temp = float(input("Enter Temperature"))


    if temp >= 20 and temp < 35.5:

        LED_swap(yellowled, redled, greenled, blueled)

    elif temp >= 35.5 and temp < 37.5:

        LED_swap(yellowled, redled, blueled, greenled)

    elif temp >= 37.5 and temp < 40:

        LED_swap(blueled, redled, greenled, yellowled)

    elif temp >= 40 and temp <= 50:

        LED_swap(yellowled, blueled, greenled, redled)
        LED_flash(redled)

    else:

        blueled.off()
        greenled.off()
        redled.off()
        yellowled.off()
        
##        print("error, out of range")
        

    
        
        
        
    
