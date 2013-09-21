#!/usr/bin/env python

#Relay Switch Trial Module
#8/17/2013

#To tell pi by user selection which relay to switch.


#Global Variables
import wiringpi2
state1=0
state2=0
state3=0
state4=0
userChoice=0
quitTrig=0

def main():
    queryRelayStatus()
    relaySwitch(0)
    
def queryRelayStatus(): # For getting Relay Status from Pi    
    global state1
    global state2
    global state3
    global state4
    state1=readPinStatus(0,0)
    state2=readPinStatus(0,1)
    state3=readPinStatus(0,2)
    state4=readPinStatus(0,3)
def readPinStatus(state,pin):
    state = wiringpi2.digitalRead(pin)
    return state
    
def relaySwitch(q):
    global userChoice
    global quitTrig
    if q==0:#Quit
        quitTrig=0
    else:
        quitTrig=1
        

    while (quitTrig == 1):
        outputRelayStatus()
        print("Press 0 to quit or...")
        userChoice = int(input("Enter which switch you want to change:"))
        makeChange()
    
def outputRelayStatus():#Assign text strings based on relay status
    s1=""
    s2=""
    s3=""
    s4=""
    if state1 == 0:
        s1 = "Off"
    else:
        s1 = "On"
    if state2 == 0:
        s2 = "Off"
    else:
        s2 = "On"
    if state3 == 0:
        s3 = "Off"
    else:
        s3 = "On"
    if state4 == 0:
        s4 = "Off"
    else:
        s4 = "On"
    displayRelayStatus(s1,s2,s3,s4)
def displayRelayStatus(r1,r2,r3,r4):
    refreshScreen()
    print("Relay  / Status: ")
    print(" One   = ",r1)
    print(" Two   = ",r2)
    print(" Three = ",r3)
    print(" Four  = ",r4)
    print("")

def makeChange(): #Evaluate user choice and make change
    global state1
    global state2
    global state3
    global state4
    global quitTrig
    if userChoice == 0:
        quitTrig = 0
        print ("")
        print ("")
        print ("")
        
    elif userChoice == 1:
        if state1 == 1:
            state1=0
            wiringpi2.digitalWrite(0,1)
        else:
            state1=1
            wiringpi2.digitalWrite(0,0)
    elif userChoice == 2:
        if state2 == 1:
            state2=0
            wiringpi2.digitalWrite(1,1)
        else:
            state2=1
            wiringpi2.digitalWrite(1,0)
    elif userChoice == 3:
        if state3 == 1:
            state3=0
            wiringpi2.digitalWrite(2,0)
        else:
            state3=1
            wiringpi2.digitalWrite(2,1)
    elif userChoice == 4:
        if state4 == 1:
            state4=0
            wiringpi2.digitalWrite(3,0)
        else:
            state4=1
            wiringpi2.digitalWrite(3,1)
    else:
        print ("Number must be between 0 and 4")
    
def saveChanges(): #Write changes to parameter file for use
    print('')

def refreshScreen():
    x=0
    counter =1
    for x in range(30)
    print('')
    
    
main()

