""" 
Script to generate Maple Input Files for all of the cellml files in the 'cellml' folder 
"""

import glob, os, subprocess

os.chdir('cellml')

for files in glob.glob('*.cellml'):
    print files

    command = '../../Chaste/python/pycml/translate.py -J --Wu --conf=../../Chaste/python/pycml/config.xml ' + files

    print command

    try:
        subprocess.call(command, shell=True) 
    except ValueError:
        print files + ' did not convert to Maple input properly.'
        continue
        
