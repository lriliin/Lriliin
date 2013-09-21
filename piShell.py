#!/usr/bin/env python

#import PiMation modules
import relaySwitchModule
import tempHumiModule

#Global Variables
userSelection=0
quitTrig=1
def main():
    shell()

def shell():
    global userSelection
    while (quitTrig==1):
        menu()
        userSelection = int(input('Enter Selection:'))
        userSelectGo(userSelection)
def menu():
    print('(1) Relay Control')
    print('(2) Temperature and Humidity Display')
    print('(0) Quit')

def userSelectGo(sel):
    global quitTrig
    if sel==0:
        quitTrig=0
    elif sel==1:
        relaySwitchModule.relaySwitch(1)
    elif sel==2:
        tempHumiModule.menu(1)
        print('Waiting on TempHumiDisplay to be made')
        shell()
    else:
        print('Select one of the menu items')
        
main()
