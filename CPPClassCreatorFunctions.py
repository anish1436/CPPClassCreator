#!/usr/bin/env python3

import re
import datetime

global varTypes
varTypes=[]
global varNames
varNames=[]

global Author
global creationDate
global FunctionTrimLen

global HfileIncludes
HfileIncludes=[]

global funcList
funcList=[]


now = datetime.datetime.now()	
creationDate=now.strftime("%Y-%m-%d %H:%M")
#creationDate=datetime.datetime.now()


global CPPFileIncludes
CPPFileIncludes=[]

global FunctionIncludes
FunctionIncludes=[]

# check if string is empty
def isBlank (myString):
    if myString and myString.strip():
        #myString is not None AND myString is not empty or blank
        return False
    #myString is None OR myString is empty or blank
    return True

# get input of author, include files, func prefix etc.

def getInput():
        INPUT = open("Input.txt","r")
        isHFileInclude=False
        isCPPFileInclude=False
        isFunctionHead=False
        fl = INPUT.readlines() # readlines reads the individual lines into a list
        for x in fl:
                x.strip()
                if re.match(r'\S+',x):
                       #ClassList.append(x)
                       
                       if isHFileInclude:
                              print("hfileIncludes.append");
                              if re.match(r"HFILE_INCLUDE_END",x):
                                   print("isHFileInclude set false")
                                   isHFileInclude=False ;
                                   continue
                              print(x);
                              HfileIncludes.append(x);
                              continue   
                       elif isCPPFileInclude:
                               if re.match(r"CPPFILE_INCLUDE_END",x):
                                    print("isHFileInclude set false")
                                    isCPPFileInclude=False ;
                                    continue
                               CPPFileIncludes.append(x);
                               continue
                       elif isFunctionHead:
                              if re.match(r"FUNCTION_HEAD_END",x):
                                   print("isHFileInclude set false")
                                   isFunctionHead=False ;
                                   continue
                              FunctionIncludes.append(x);
                              continue  
                           
                       if re.match(r"AUTHOR", x):
                              global  Author
                              Author=getFuncName(x)     
                              print("got author name:: ")
                              print(Author)                  
                       elif re.match(r"CLASSEND", x):
                              continue;       
                       elif re.match(r"DATE",x):
                              creationDate=getFuncName(x)
                              if (isBlank(creationDate)):
                                  now = datetime.datetime.now()	
                                  creationDate=now.strftime("%Y-%m-%d %H:%M")
                       elif re.match(r"GET_FUNCTION_PREFIX",x):
                              global getFunctionPrefix
                              getFunctionPrefix=getFuncName(x) 
                       elif re.match(r"SET_FUNCTION_PREFIX",x):
                              global setFunctionPrefix
                              setFunctionPrefix=getFuncName(x) 
                       elif re.match(r"VARIABLE_TRIM_LENGTH",x):
                              global FunctionTrimLen
                              FunctionTrimLen=int(getFuncName(x) )
                       elif re.match(r"HFILE_INCLUDE_START",x):
                              print("isHFileInclude set true")
                              isHFileInclude=True ;          
                       elif re.match(r"CPPFILE_INCLUDE_START",x):
                              isCPPFileInclude=True;
                       elif re.match(r"FUNCTION_HEAD_START",x):
                              isFunctionHead=True;
        print("HINCLUDE FILES");
        print(HfileIncludes);
        print(CPPFileIncludes)
      

def clearInput():
    HfileIncludes[:]=[]
    CPPFileIncludes[:]=[]
    FunctionIncludes[:]=[]
                        
                       
                                
                       
#clear file creation sesssion.

def clearFileSession():
        HFILE.close()
        CFILE.close()
        ClassList=[];
        varNames=[]
        varTypes=[]
        
#create code files
#==========================================================================
def  createClassFiles(className):
       
       headerFileName=className.strip()+".h"
       classFileName=className.strip()+".cpp"
       print("header file"+headerFileName+"cpp file::"+classFileName+"\n")
       
       global HFILE
       HFILE=open(headerFileName,"w+")
       global CFILE
       CFILE= open(classFileName,"w+")   
       getInput()   
       AddClassHead() 

       if HFILE.mode == 'w+':
           print("opended "+headerFileName+"Successfully author:"+Author)
           printAuthorDetails(HFILE)
           AddHeaderFileIncludes(HFILE)
           HFILE.write("class "+className+"\n{\n proteced:\n")
       else:
           print("cannot open  "+headerFileName+"Successfully")
       
       
       
       if CFILE.mode == 'w+':
           print("opended "+headerFileName+"Successfully")
           printAuthorDetails(CFILE)
           AddCPPFileIncludes(CFILE)
           CFILE.write("class "+className+"\n{\n protected:\n")
       else:
           print("cannot open  "+headerFileName+"Successfully")
#==========================================================================
# close class files
def   closeClassFiles():
              HFILE.write("\n};\n")
              CFILE.write("\n};\n")


#==========================================================================



# Add class outline
def   AddFunc(funcName,retType):

       print("Function include list")
       print(FunctionIncludes)
       for i in FunctionIncludes:
          HFILE.write(i)
          CFILE.write(i)
       HFILE.write("\t"+retType+" "+ funcName+"();\n")
       CFILE.write("\t"+retType+" "+className.strip('\n')+"::"+funcName+"()\n")
       CFILE.write("{\n}\n") 
       
#==========================================================================

# Add variable.
def   AddVar(Type,Value):
       varTypes.append(Type)
       varNames.append(Value)
       CFILE.write("\t"+Type+" "+Value+";\n")
       HFILE.write("\t"+Type+" "+Value+";\n")

#==========================================================================
# add default .h files includes
def AddHeaderFileIncludes(HFILE):
     #  Temp= open("HfileIncludes.txt","r+")
      # fl = Temp.readlines() # readlines reads the individual lines into a list
    print("INSIDE addheaderfileIncludes")
    print(HfileIncludes)
    for x in HfileIncludes:
       HFILE.write(x)
      # Temp.close()
#==========================================================================
# add default .h files includes
def AddCPPFileIncludes(CFILE):
   # Temp= open("CppfileIncludes.txt","r+")
   # fl = Temp.readlines() # readlines reads the individual lines into a list
    print(CPPFileIncludes)
    for x in CPPFileIncludes:
        CFILE.write(x)
    #Temp.close()
#==========================================================================
# add write/read/copy in class files
def  AddDefaultHeaderfileFuncs():
      # HFILE.write("\t"+className+"(const"+className+"& rhs);\n")
      # HFILE.write("\t"+className+"& operator=(const"+className+"& rhs);\n")
      # HFILE.write("\tvirtual ~"+className+"();")
      # HFILE.write("\tMavObjectLength ::writeObject(unsigned char* pBuf, u32_t bufLen);\n")
      # HFILE.write("\tMavObjectLength readObject(unsigned char* pBuf, u32_t bufLen);\n")
      # HFILE.write("\tvoid printObject();\n") 
#==========================================================================
# add write/read/copy in class files

#def  AddDefaultFunctions():
      """AddDefaultHeaderfileFuncs() 
      CFILE.write("public:\n"+className+"::"+className+"(const"+className+"&rhs)\n")
      CFILE.write("{\n")
      print("varNames before writing into file len"+str(len(varNames)))
      #print(varNames)
      for i in  range(len(varNames)):
            CFILE.write("\t"+varNames[i]+"=rhs."+varNames[i]+";\n")
      CFILE.write("}\n")


     
      CFILE.write("MavObjectLength "+className+ "::writeObject(unsigned char* pBuf, u32_t bufLen)\n{\n")
      CFILE.write("\tsetCurrentPtr(pBuf, bufLen);\n")
      for i in range(len(varNames)):
          CFILE.write("\tmavWrite("+varNames[i]+");\n")
      CFILE.write("\treturn getCurrentLen();\n}\n")

     
      CFILE.write("\tMavObjectLength "+className+"::readObject(unsigned char* pBuf, u32_t bufLen)\n{\n")
      CFILE.write("\tsetCurrentPtrAndLen(pBuf, bufLen);\n")
      for i in range(len(varNames)):
          CFILE.write("\tmavRead("+varNames[i]+");\n")
      CFILE.write("\treturn getCurrentLen();\n}\n")
      

     
      CFILE.write("\tvoid"+className+"::printObject()\n{\n}\n")
      varNames[:] = []
      """
      
#==========================================================================

# Add CLASS TOPS.
def   AddClassHead():
       htF=open("HTop.txt","r")
       htV=htF.readlines()
       for x in htV:
          x.strip()
          HFILE.write(x)
          CFILE.write(x)
       
          
       

# create header file
#==========================================================================
#def createHeaderFile()



#==========================================================================

# create CPP file
#==========================================================================
#def createCPPFile()



#==========================================================================

# print the Author details
#==========================================================================
def printAuthorDetails(inputFILE):
       now = datetime.datetime.now()
       inputFILE.write("//****************************************************************************************\n")
       datevalue=now
       if len(creationDate.strip()) != 0:
               datevalue=creationDate
       inputFILE.write("// Author::"+ Author +" \n // Date:: "+datevalue+"\n")
       inputFILE.write("// Description:\n")
       inputFILE.write("// \n")
       inputFILE.write("// \n")
       inputFILE.write("//****************************************************************************************\n")
#==========================================================================
       
# fetch class name string
#==========================================================================
def getClassName(value):
      colonPos=value.split(":")
      return colonPos[1]
#==========================================================================

# fetch Function name string
#==========================================================================
def getFuncName(value):
      print("getfun name ",value) 
      colonPos=value.split(":")
      return colonPos[1]
#==========================================================================

# handle class creation from list of lines!!!
def handleClassListInput(list):
     print(list)
     getInput()     
     for x in list:
          x.strip()
          if re.match(r"CLASS_NAME", x):
                global className
                className = getClassName(x)
                createClassFiles(className)
               
                print("\nClass name"+className)
                
                continue
          elif re.match(r"FUNC", x):
##                funcName=getFuncName(x)
##                print("Func name"+funcName)
##                OUTPUT.write(funcName)
##                OUTPUT.write(";\n")
##                funcName=""
                continue
              
          elif re.match(r"CLASS_END",x):
                continue
          if len(x.strip()) != 0:
              getList=x.split()
              if ((len(getList[0])>0) and (len(getList[1])>0)):

                       AddVar(getList[0],getList[1])
                       
              getList=[]
              var=""
              
     #funclist=[] 
     global funcList
     funcList=[] 
     for x in list:
              x.strip()
              if re.match(r"CLASS_NAME", x):
                    continue
              elif re.match(r"FUNC", x):
                    funcList.append(x)
                    continue
              elif re.match(r"CLASS_END",x):
                continue
              if len(x):
                getList=x.split()
                print("function trim lent::")
                print(FunctionTrimLen)
                if (len(getList[0]) and len(getList[1])):
                             #tempFunPre=
                             getS=getList[0]
                             preFix= getFunctionPrefix if(len(getFunctionPrefix)) else "get"
                             getS+=" "+preFix.strip('\n')
                             print("list[0]")
                             print(getList[0])
                             print("list[1]")
                             print(getList[1])
                             varname=getList[1]
                             funcN= varname[FunctionTrimLen:] if(FunctionTrimLen>0) else varname
                             funcN=getList[1]
                             getS+=funcN
                             getS+="()\n\t{\n\t\t"+"return "
                             getS+=getList[1]+" ;\n\t}\n"
                             setS="void  " 
                             preFix=  setFunctionPrefix if(len(setFunctionPrefix)) else "set" 
                             setS+=preFix.strip("\n")
                             funcN=varname[FunctionTrimLen:] if(FunctionTrimLen>0) else varname
                             setS+=funcN
                             setS+="("+getList[0]+" input)\n\t{\n\n\t\t"+"m"+getList[1][int(FunctionTrimLen):]+"= input;\n\t}\n"
                             HFILE.write(getS)
                             HFILE.write(setS)
                getS=""
                setS=""
                getList=[]
     for i in funcList:
              i.strip()
              print(funcList)
             # if re.match(r"FUNC", x):

              funcName=getFuncName(i)
              print("Function::"+funcName+"\n")
              fList=funcName.split()
              AddFunc(fList[1],fList[0])
     closeClassFiles()
     
              #continue
     #AddDefaultFunctions()
     print("varNames list::")
     funcList=[];
     ClassList=[];
     varNames=[];
     varTypes=[];
     print (varNames)
     clearFileSession()
     
# END of handle class input
              
