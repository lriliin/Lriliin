#!/usr/bin/env python

#(c)PiMation LLC
# 9/5/2013
#Temperature Humidity Trial Program
#

#Global Variables
userSelection=0
quitTrig=0
currentTemp=0
currentHumi=0
targetTemp=0
targetHumi=0
targetTempVar=0
targetHumiVar=0

def main():
    menu(0)
    
def menu(q):
    global userSelection
    global quitTrig
    if q==0:#Quit
        quitTrig=0
    else:
        quitTrig=1
    while(quitTrig==1):       
        print('(1) Display Temperature and Humidity')
        print('(2) Set Temperature Target')
        print('(3) Set Humidity Target')
        print('(4) Diagnostics')
        print('(0) Quit')
        userSelection = int(input('Enter Selection:'))
        userSelectGo(userSelection)


def userSelectGo(sel):
    global quitTrig
    if sel==0:
        quitTrig=0
    elif sel==1:
        displayTempHumi(currentTemp,currentHumi)
        cont()
    elif sel==2:
        setTargetTemp()
    elif sel==3:
        setHumiTarget()
    elif sel==4:
        diagnoseHumiTemp()
    else:
        print('Select one of the menu items')

def displayTempHumi(h,t):    
    print('Current Temperature: ',format(currentTemp, '.1f'),'F')
    print('Current Humidity: ',format(currentHumi,'.1f'),'%')
    

def setTargetTemp():
    change=''
    print('Current Temperature is: ',format(currentTemp, '.1f'),'F')
    print('Current Target is: ',format(targetTemp,'.1f'),'F')
    print('Current Target variance is +/-: ',format(targetTempVar,'.1f'),'F')
    print('')
    while not(change == 'y')or(change=='n'):
        change = (input('Change target temperature? (y)es or (n)o: '))
        if change=='y':
            change=='n'
            selectNewTemp()
            selectNewTempVar()
        elif change=='n':
            break
    
def selectNewTemp():
    global targetTemp
    targetTemp= float(input('Enter new target temperature: '))
    
def selectNewTempVar():
    global targetTempVar
    targetTempVar = float(input('Enter new acceptable variance for temperature: '))

def setHumiTarget():
    change=''
    print('Current Humidity is: ',format(currentHumi, '.1f'),'%')
    print('Current Target is: ',format(targetHumi,'.1f'),'%')
    print('Current Target variance is +/-: ',format(targetHumiVar,'.1f'),'%')
    print('')
    while not(change == 'y')or(change=='n'):
        change = str(input('Change target humidity? (y)es or (n)o: '))
        if change=='y':
            change=='n'
            selectNewHumi()
            selectNewHumiVar()
        elif change=='n':
            break
        
def selectNewHumi():
    global targetHumi
    targetHumi= float(input('Enter new target humidity: '))

def selectNewHumiVar():
    global targetHumiVar
    targetHumiVar = float(input('Enter new acceptable variance for humidity: '))
    
def diagnoseHumiTemp():
    print('This is where all the technical shit for the probe is.  Like raw readings and stuff')
    


def cont(): #To pause screen 
    cont =''
    cont = input('Press Enter to continue...')

def saveChanges(): #save changes to parameter file for use.
    print('')










main()
