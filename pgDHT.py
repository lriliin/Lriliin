#!/usr/bin/python

import subprocess
import re
import time

#Global Variables
temp=0
humi=0

def main():
    x=0
  while (x==0):    
    output = subprocess.check_output(["./Adafruit_DHT", "22", "4"]);
    print output
    matches = re.search("Temp =\s+([0-9.]+)", output)
    if (not matches):
        time.sleep(3)
        continue
    temp = float(matches.group(1))

    matches = re.search("Hum =\s+([0-9.]+)", output)
    if (not matches):
        time.sleep(3)
        continue
    humi = float(matches.group(1))

    
    print "Temeperature: %.1f C" % temp
    print "Humidity: %.1f %%" % humi
    gonogo=0
    gonogo = int(input("press numeral 1 to quit"))
    if gonogo = 1:
        break
    else:
        x=0
        return
main()

                        
    
 
