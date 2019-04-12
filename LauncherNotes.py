'''
Created on Apr 11, 2019

@author: darrenbean
'''


import subprocess

"""
calcProc = subprocess.Popen('C:\\windows\\System32\\calc.exe')
# return value is Popenobject
# methods: poll() and wait()
print(calcProc.poll())
print(calcProc.wait())
"""

#can pass args -- this opens notepad, which then opens hello file
subprocess.Popen(['C:\\Windows\notepad.exe', 'C:\\hello.txt'])
# can use this to launch python scripts 
subprocess.Popen(['C:\\python34\python.exe', 'hello.py'])
# can use (['start', ...], shell=True) to use default program
