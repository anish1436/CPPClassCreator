# CPPClassCreator
quite a bit of time is spent on creating header(.h) and cpp/hpp files, defining setters/getters for member variables,putting author description,
license information, function description blocks etc. takes time if done manually/typed. 
this is a python tool to create class files with necessary information,
getters/setters for member variables are created based on input class template.
all the information needed to create the classes like author/date, function description block, license information etc. needs to be put in 
the Input.txt file.
the basic class template is of below format(described in the Input.txt files)
any number of required class information can be provided in below format in the Input.txt

CLASS_NAME:AbChangesNotificationData
FUNC: void writeObject(int n, char * data)
FUNC: void readObject(char * s,int len)
u32_t                    mDuration
MavString                mCallbackData   
PresenceResourceStatus_e mResourceStatus
LinkData                 mLinkData
LinkDataList             mLinkDataList
CLASS_END


CLASS_NAME:AbChangesNotificationData2
FUNC: void writeObject(int n, char * data)
FUNC: void readObject(char * s,int len)
u32_t                    mDuration
MavString                mCallbackData   
PresenceResourceStatus_e mResourceStatus
LinkData                 mLinkData
LinkDataList             mLinkDataList
CLASS_END


for each of the classes header and cpp files with setters/getters, header files provided as input and other description blocks are added to all 
of the class files that are created

fill in the Input.txt file in the same folder as the python scripts and invoke the CreateCPPClass.py script... the class files are created
in the same folder
