'''
Created on Apr 4, 2019

@author: darrenbean
'''

import json

stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'
jsonDataAsPythonValue = json.loads(stringOfJsonData)
#need to use .loads ("load string") to convert Json string to python dict
#Json always uses double quotes
#order may differ b/t Py and Json
print(jsonDataAsPythonValue)

pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}
stringOfJsonData = json.dumps(pythonValue)
#dumpstring writes Json string value
print(stringOfJsonData)