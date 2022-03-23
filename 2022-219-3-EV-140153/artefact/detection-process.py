# MBTechWorks.com 2017
# Use an HC-SR501 PIR to detect motion (infrared)

#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import os
from datetime import datetime


GPIO.setmode(GPIO.BOARD) #Set GPIO to pin numbering
pir = 8 #Assign pin 8 to PIR
led = 10 #Assign pin 10 to LED
GPIO.setup(pir, GPIO.IN) #Setup GPIO pin PIR as input
GPIO.setup(led, GPIO.OUT) #Setup GPIO pin for LED as output
print ("Sensor initializing . . .")
time.sleep(2) #Give sensor time to startup
print ("Active")
print ("Press Ctrl+c to end program")
presentime = datetime.now()
print("Current timestamp info...")
print(presentime)
print("----")
#Set a sample value for motion...
motion="1" 
still="2"


try:
    while True:
        if GPIO.input(pir) == True: #If PIR pin goes high, motion is detected
            print ("Motion Detected!")
            presentime = datetime.now()
            GPIO.output(led, True) #Turn on LED
            time.sleep(0.5) #Keep LED on for 4 seconds
#            os.system('sqlite3 db/sensordata.db')       
#            os.system('BEGIN;')
#            os.system('INSERT INTO pirreadings(currentdate, currenttime, motion) values(date("now"), time("now"), "1");')
#            os.system('COMMIT')
#            os.system('sqlite3 db/sensordata.db "BEGIN;"')
#            os.system('sqlite3 db/sensordata.db "INSERT INTO pirreadings(currentdate, currentime, motion) values(date(presentime), time(presentime), "1");"')
            GPIO.output(led, False) #Turn off LED
            print("Insert using python date/time functions....")
            cmd='sqlite3 db/sensordata.db \'INSERT INTO pirreadings(currentdate, currentime, motion) values("%s","%s","%s");\'' % (datetime.date(presentime),datetime.time(presentime),motion)
            print(cmd)
            os.system(cmd)             
            time.sleep(60)
        if GPIO.input(pir) == False: #If PIR pin goes high, motion is detected
#            os.system('sqlite3 db/sensordata.db')
#            os.system('BEGIN;')
#            os.system('INSERT INTO pirreadings(currentdate, currenttime, motion) values(date("now"), time("now"), "0");')
#            os.system('COMMIT')
#            os.system('sqlite3 db/sensordata.db "BEGIN;"')
#            os.system('sqlite3 db/sensordata.db "INSERT INTO pirreadings(currentdate, currentime, motion) values(date("now"), time("now"), "0");"')
            presentime = datetime.now()
            print("Insert using python date/time functions....")
            cmd='sqlite3 db/sensordata.db \'INSERT INTO pirreadings(currentdate, currentime, motion) values("%s","%s","%s");\'' % (datetime.date(presentime),datetime.time(presentime),still)
            print(cmd)
            os.system(cmd)


except KeyboardInterrupt: #Ctrl+c
    os.system('sqlite3 db/sensordata.db "COMMIT;"')
    pass #Do nothing, continue to finally

finally:
    GPIO.output(led, False) #Turn off LED in case left on
    GPIO.cleanup() #reset all GPIO    



#Create the table if it isn't there. I guessed datatypes
#cmd="CREATE TABLE IF NOT EXISTS pirreadings ( currentdate TEXT, currentime TEXT, motion TEXT);"
#print(cmd)
#os.system('sqlite3 db/sensordata.db \'%s\'' % cmd)


#Using sqlite3's own functions to get current date and time ...
#print("Insert using sqlite date/time functions....")
#os.system('sqlite3 db/sensordata.db "INSERT INTO pirreadings(currentdate, currentime, motion) values(date(), time(), "1");"')
#print("----")
#print("Checking what's in the db now...")
#os.system('sqlite3 db/sensordata.db "select * from pirreadings;"')

