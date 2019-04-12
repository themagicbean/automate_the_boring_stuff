#! python3
# bulletPointAdder.py adds bullets to text in list

'''
Created on Jan 28, 2019

@author: darrenbean
'''

import pyperclip
text = pyperclip.paste()

lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
    
text = '\n'.join(lines)
#needed to make list back into a string for pyperclip.copy

pyperclip.copy(text)

print(text)
