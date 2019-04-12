'''
Created on Apr 11, 2019

@author: darrenbean
'''
import time, subprocess

timeLeft = 60
while timeLeft > 0:
    print(timeLeft, end='')
    time.sleep(1)
    timeLeft = timeLeft - 1
    
subprocess.Popen(['start', 'alarm.wav'], shell=True)

