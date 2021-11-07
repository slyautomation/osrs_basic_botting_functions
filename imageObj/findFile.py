import os
import re
from pathlib import Path

#TODO: add the name of the assets folder to the end of path or require the asset folder as an argument
def getFile(Name:str):
    filesList = searchDirectory()
    for x, File in enumerate(filesList):
        if Name in File:
            return File

def searchDirectory():
    path = str(Path.cwd()) + '\\assets'
    imageInpathNameRE = re.compile(r".png$")
    files = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        
       continue

    for i in range(len(filenames)):
        fileCheck = imageInpathNameRE.search(filenames[i])
        
        if fileCheck:
            files += [path + '\\' + filenames[i]]

    files = sorted(files)
    return files
