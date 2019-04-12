'''
Created on Apr 2, 2019

@author: darrenbean
'''
import csv  
exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)

"""
print(exampleData)
print(exampleData[0][0])  # row, column
print(exampleData[6][1])
"""

"""
rownum = 1
for row in exampleData:
    print('Row #' +str(rownum) + ' ' + str(row))
    rownum += 1
    # ATBS gave str(exampleReader.line_num), but that gives total lines
    # exampleData.line_num gives data type attribute error
"""

"""
outputFile = open('output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
outputWriter.writerow(['Hello World!', 'pizza', 'sausage', 'taco'])
outputWriter.writerow([1, 2, 3, 3.14159, 4])
outputFile.close()
"""

csvFile = open('example.tsv', 'w', newline='')
#delimiter is char that separates vars, terminator @ end of line
csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')
csvWriter.writerow(['apples', 'oranges', 'grapes'])
csvWriter.writerow(['eggs', 'bacon', 'ham'])
csvWriter.writerow(['spam', 'spam', 'spam', 'spam', 'spam'])
csvFile.close()
                       
    