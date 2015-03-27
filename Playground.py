__author__ = 'jjtriplei'

import os

#feels unnecessary
path = "/usr/bin/"
dirs = os.listdir(path)

if "overviewer.py" in dirs:
  print ("Yes")
    else:
    print ("No")