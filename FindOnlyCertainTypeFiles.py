#! python3
# backs up only .py files
# holy shit it works
# would be better with input to get file type and folder name

'''
Created on Feb 13, 2019

@author: darrenbean
'''

import shutil, os

def findOnlyCertainFiles(folder):
    folder = os.path.abspath(folder)
    
    if not os.path.isdir(folder + r'\pythonbackup'):
        os.makedirs(folder + r'\pythonbackup')
        
    backupLocus = str(folder + r'\pythonbackup')
    
    for foldername, filenames in os.walk(folder):
        print("Scanning for and copying selected type of files in %s ... " % (foldername))
        for filename in filenames:
    
            # set up to backup only py files
            if filename.endswith('py'):
                shutil.copy(filename, backupLocus)
            
    print('Done.')
    
findOnlyCertainFiles(r"C:\Users\darrenbean\eclipse-workspace\AutomateTheBoringStuff")        