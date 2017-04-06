import os
from datetime import datetime
#print(dir(os)) #all mathods of OS module
print(os.getcwd()) #get current working direcory
os.chdir('/home/manish/code')#change directory
#print(os.listdir()) #list directories on current directories
#os.mkdir('mydir') # To create directory
#os.makedirs('mydir2/newdir')#To make more than one level of dirs
#os.rmdir('mydir')#delete dir
#os.removedirs('mydir2/newdir')
#print(os.stat('test3')) #complete info about file
#mod_time = os.stat('test3').st_mtime
#print(datetime.fromtimestamp(mod_time))#Last modified time
#os.rename('test2','fake') #To rename file
#print(os.listdir())
print(os.environ.get('/home/manish/code'))
#os.walk gives complete tree of directory treversing all dir & subdir in folder
for dirpath,dirnames,filenames in os.walk('/home/manish/code'):
	print('Current Path: ',dirpath)
	print('Directories:',dirnames)
	print('Files:',filenames)
print(os.path.exists('/home/manish/code'))#To check if a path exist or not
print(os.path.isfile('/home/manish/code/1.cpp'))#To check if a file exist or not
print(dir(os.path)) #print all functionality of os.path