'''
Created on Feb 4, 2019

@author: darrenbean
'''
"""
helloFile = open('C:\\Users\\darrenbean\\eclipse-workspace\\AutomateTheBoringStuff\\hello.txt')
helloContent = helloFile.read()
print(helloContent)

sonnetFile = open('C:\\Users\\darrenbean\\eclipse-workspace\\AutomateTheBoringStuff\\sonnet29.txt')
print(sonnetFile.readlines())
"""

"""
baconFile = open('bacon.txt', 'w')
baconFile.write('Hello World!\n')
baconFile.close()

baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.')
baconFile.close

baconFile = open('bacon.txt')
content = baconFile.read()
baconFile.close()
print(content)
"""

"""
import shelve
shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
print(cats)
shelfFile.close()

shelfFile = shelve.open('mydata')
print (list(shelfFile.keys()))
print (list(shelfFile.values()))
shelfFile.close()
"""

"""
import pprint
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
print(pprint.pformat(cats))

fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close() # need to get out of write mode
fileObjR = open('myCats.py', 'r')
catContent = fileObjR.read()
print(catContent)
fileObjR.close()
# needed to re
"""

"""
import myCats
print(myCats.cats)
"""



