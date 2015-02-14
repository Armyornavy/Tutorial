import os
os.mkdir
try:
   f = open("file.txt.", "w")
except IOError:
    print('An error has occured while trying to use this file.')
