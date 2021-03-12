import os
import xlrd
from datetime import datetime


filename = 'generated_playlist'


# Find files to import from import folder

filelist = os.listdir("audio")
print(filelist)

if len(filelist) == 0:
    print("Directory is empty \nExit application")
    quit() #end script

else:
    print("Reading files")
    f= open(f"{filename}.txt","w+")


    for filename in filelist:
        #Start write to file
        f.write("\t\t{\n")
        f.write(f'\t\t\ttitle:"{filename}",\n')
        f.write(f'\t\t\twav:"audio/{filename}"\n')
        f.write("\t\t},\n")
        

f.close() 



