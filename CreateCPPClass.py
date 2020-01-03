#!/usr/bin/env python3

#
# Read and write files using the built-in Python file methods
#
import re
import datetime
import sys
import CPPClassCreatorFunctions as F

# class file names
headerFileName=""
classFileName=""
##HFILE=''
##CFILE=''
#ClassList=[]


fileSetStarted=0
fileSetComplete=0

#open files

if len(sys.argv) < 2:
    INPUT = open("Input.txt","r")
else:
    INPUT = open(sys.argv[1],"r")
      

OUTPUT = open("Out.txt","w+")


      
def main():  
    # Open a file for writing and create it if it doesn't exist
      #isClassStarted=false;
      if INPUT.mode == 'r': # check to make sure that the file was opened
        # use the read() function to read the entire file
        # contents = f.read()
          # print (contents)
        global ClassList
        fileSetStarted=0
        ClassList=[];
        fl = INPUT.readlines() # readlines reads the individual lines into a list
        for x in fl:
                x.strip()
                if re.match(r'\S+',x):
                       if fileSetStarted==1:
                        ClassList.append(x)
                       if re.match(r"CLASS_NAME", x):
                              fileSetStarted=1  
                              ClassList.append(x)                     
                              continue
                       elif re.match(r"CLASS_END",x):
                              ClassList.append(x) 
                              fileSetStarted=0
                              F.handleClassListInput(ClassList)
                              print(ClassList)
                              ClassList=[]
                              #varNames[:] = []
                              continue                                      

        INPUT.close()
        
    
if __name__ == "__main__":
  main()
