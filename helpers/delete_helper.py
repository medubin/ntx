import os
import shutil

def note(filepath):
    os.remove(filepath) 

def folder(folderpath):
    shutil.rmtree(folderpath)