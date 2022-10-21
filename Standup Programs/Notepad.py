# import subprocess module
import subprocess as sp

'''
A program can create new processes using library functions such as those found in the os 
or subprocess modules such as os.fork(), subprocess.Popen(), etc. However, these processes, 
known as subprocesses, run as completely independent entities-each with their own private 
system state and main thread of execution.
'''

# name program you want to open

programname = "Notepad.exe"

# name file
filename = "Myfile.txt"
sp.Popen([programname,filename])