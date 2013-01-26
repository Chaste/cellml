""" 
Script to generate Maple Input Files for all of the cellml files in the 'cellml' folder 
"""

import glob, os, subprocess

os.chdir('cellml')

for files in glob.glob('*.mpl'):
    print files

    command = 'maple -i ' + files + ' > ' + files[:-3] + 'out' 

    print command

    subprocess.check_call(command, shell=True) 

        
