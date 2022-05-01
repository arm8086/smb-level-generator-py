import os
import requests
import namegen
path2 = ".\\level-headed\\"
def replaceLine(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()
def readLine(file_name, line_num):
    lines = open(file_name, 'r').readlines()
    return lines[line_num]
oldPath = readLine(path2+"Config\\SMB1_Compliance_To_SMB1.cfg", 104)
oldStat = readLine(path2+"Config\\SMB1_Compliance_To_SMB1.cfg", 105)
oldMN = readLine(path2+"Config\\SMB1_Compliance_To_SMB1.cfg", 95)
oldLN = readLine(path2+"Config\\SMB1_Compliance_To_SMB1.cfg", 96)
marioName = namegen.randomName(1)[0]
luigiName = namegen.randomName(1)[0]
print(marioName, luigiName)
replaceLine(path2+"Config\\SMB1_Compliance_To_SMB1.cfg", 104, "Output_ROM_Location=C:\\tmp\\smb1.nes\n")
replaceLine(path2+"Config\\SMB1_Compliance_To_SMB1.cfg", 105, "Overwrite_Output_ROM=true\n")
replaceLine(path2+"Config\\SMB1_Compliance_To_SMB1.cfg", 95, "Luigi_Name="+marioName+"\n")
replaceLine(path2+"Config\\SMB1_Compliance_To_SMB1.cfg", 96, "Mario_Name="+luigiName+"\n")
os.system("\""+path2+"Level-Headed.exe\" -i SMB1_Compliance_To_SMB1")
replaceLine(path2+"Config\\SMB1_Compliance_To_SMB1.cfg", 104, oldPath)
replaceLine(path2+"Config\\SMB1_Compliance_To_SMB1.cfg", 105, oldStat)
replaceLine(path2+"Config\\SMB1_Compliance_To_SMB1.cfg", 95, oldMN)
replaceLine(path2+"Config\\SMB1_Compliance_To_SMB1.cfg", 96, oldLN)
os.system(".\\emulator\\mesen.exe C:\\tmp\\smb1.nes /fullscreen /Region=Auto /DoNotSaveSettings")
os.remove("C:\\tmp\\smb1.nes")