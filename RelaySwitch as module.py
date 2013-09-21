#Relay Switch Trial Program
#8/17/2013

#To tell pi by user selection which relay to switch.


#Global Variables
state1=0
state2=0
state3=0
state4=0
userChoice=0
quitTrigger = 1

#main program

def main():
    relaySwitch()
    
def relaySwitch():
    print("Press 0 to quit")
    outputRelayStatus()# Tell what state each relay is in

    #Request user input
    global userChoice
    global quitTrigger
    while (quitTrigger == 1):
        userChoice = int(input("Enter which switch you want to change:"))
        changeOutput()
        outputRelayStatus()
#def queryPiRelayStatus():#For use with actual relay
    
def outputRelayStatus():#Output Relay Status
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
    print("Relay  / Status: ")
    print(" One   = ",s1)
    print(" Two   = ",s2)
    print(" Three = ",s3)
    print(" Four  = ",s4)
    print("")

def changeOutput(): #Evaluate user choice and make change
    global state1
    global state2
    global state3
    global state4
    global quitTrigger
    if userChoice == 0:
        quitTrigger = 0
        print ("")
        print ("")
        print ("")
        
    elif userChoice == 1:
        if state1 == 1:
            state1=0
        else:
            state1=1
    elif userChoice == 2:
        if state2 == 1:
            state2=0
        else:
            state2=1
    elif userChoice == 3:
        if state3 == 1:
            state3=0
        else:
            state3=1
    elif userChoice == 4:
        if state4 == 1:
            state4=0
        else:
            state4=1
    else:
        print ("Number must be between 0 and 4")
    

main()
