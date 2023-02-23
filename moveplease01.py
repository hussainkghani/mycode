#!/usr/bin/env python3

import shutil
import os

#force program to start in home directory
os.chdir('/home/student/mycode/')

#calling shutil.move will move the file or folder at the path source to the path destination and return a string of the absolute path of the new location
shutil.move('raynor.obj', 'ceph_storage/')

#prompt user for a new name for the kerrigan.obj
xname = input('What is the new name for kerrigan.obj? ')

#rename the current kerrigan.obj file
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)


