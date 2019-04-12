'''
Created on Jan 24, 2019

@author: darrenbean
'''
"""
spam = ['apples', 'bananas', 'tofu', 'cats']
numberage = ['1', '2', '3', '4', '5', '6']

def listToString(list_to_be_strung):
    listlen = len(list_to_be_strung)
    listbeforeand = listlen - 2
    listendage = listlen - 1
    listitem = 0
    while listitem < listbeforeand:
        print(str(list_to_be_strung[listitem]) + ", ", end='')
        listitem += 1
    print(list_to_be_strung[listbeforeand] + ", and " + \
          list_to_be_strung[listendage])


# this would be main for ex 1, above, which works fine
      
listToString(spam)
listToString(numberage)
"""

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def printThatGrid(the_grid):
    elements = len(the_grid[0]) 
    columns = len(the_grid) 
    # easy because all sublists same size 
    
    i = 0
    while i < elements:
        j = 0
        while j < columns:
            print((the_grid[j][i]), end = '')
            j += 1
        i += 1
        print('\n', end = '')
    
printThatGrid(grid)
    