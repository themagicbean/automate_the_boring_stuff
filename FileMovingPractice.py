'''
Created on Feb 12, 2019

@author: darrenbean
'''

import shutil, os, send2trash, zipfile


# be careful when using move - can overwrite or assume
# you intended a file name not folder, etc.

# need shutil.rmtree(path) to remove path & all its contents
# os.rmdir(path) will just delete the folder, which must be empty
# os.unlink(path) will delete a file
# rmtree = irreversible deletion?
# send2trash module just sends to recycle bin
# which will not free up disk space


#for folderName, subfolders, filenames in os.walk(r'C:\Users\darrenbean\eclipse-workspace\AutomateTheBoringStuff'):
#    print('The current folder is ' + folderName)


newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('bacon.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.write('Madlib1.txt', compress_type=zipfile.ZIP_DEFLATED)
#newZip.close()

baconInfo = newZip.getinfo('bacon.txt')
print(baconInfo.file_size)
print(baconInfo.compress_size)

print(newZip.namelist())

newZip.extractall(r'C:\Users\darrenbean\eclipse-workspace\AutomateTheBoringStuff\src\newZipExtracted')
newZip.close()





