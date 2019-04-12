'''
Created on Apr 4, 2019

@author: darrenbean
'''

import csv, os

os.makedirs('headerRemoved', exist_ok=True)

for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue #skip the file
    
    print('Off with its header! ' + csvFilename + ' ...')
    
    # go through rows, skip 1st (header), copy rest
    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue # skip the row
        csvRows.append(row)
    csvFileObj.close()
    
    # write out
    csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w',
                      newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()
    
    