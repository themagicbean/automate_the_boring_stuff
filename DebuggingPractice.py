'''
Created on Feb 13, 2019

@author: darrenbean
'''


"""
def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception("Symbol must be single character string.")
    
    if width <= 2:
        raise Exception("Width must be greater than 2.")
    
    if height <+ 2:
        raise Exception("Height must be greater than 2.")
    
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)
    
for sym, w, h in (("*", 4, 4), ("O", 20, 5), ("x", 1, 3), ("ZZ", 3, 3)):
    try:
        boxPrint(sym, w, h)
    except Exception as err:
        print("An exception happened: " + str(err))
"""

"""
import traceback
try:
    raise Exception("This is the error message.")
except:
    errorFile = open('errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc()) # this is how to get traceback as str
    errorFile.close()
    print('The traceback info was written to errorInfo.txt')
"""

"""
market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}

def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'
    
    assert 'red' in stoplight.values(), "Neither light is red!" + str(stoplight)

switchLights(market_2nd)
"""

"""
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s)' % (n))
    return total

print(factorial(5))
logging.debug('End of program')

# logging.disable(logging.CRITICAL) to disable all logging 
"""

"""
import logging
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

# writes log to .txt file
"""



