import ctypes  # For Mbox
import sys # For exit
def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

fileIn = "in.fdf"
fileOut = "out.fdf"
fileReplace = "replace.txt"

MB_OK = 0
MB_OKCANCEL = 1

IDCANCEL = 2

try:
    f = open(fileIn,'r')
    filedata = f.read()
    f.close()
except IOError:
    Mbox('IOError', 'The file ' + fileIn + ' cannot be opened', MB_OK)
    sys.exit()

try:
    with open (fileReplace,'r') as fReplace:
        textReplace = fReplace.readlines()
except IOError:
    Mbox('IOError', 'The file ' + fileReplace + ' cannot be opened', MB_OK)
    sys.exit()
    
lineNum = 0
replaces = []

for line in textReplace:
    lineNum = lineNum + 1
    findReplace = line.split()
    bAllow = False

    for i, word in enumerate(findReplace):      
        if i == 0:
            textReplace = word.strip()
            replaces.append(textReplace)
        elif i == 1:
            textFind = word.strip()
            bAllow = True # Two parameters need for replacement
        else:
            print("The word '" + word.strip() + "' was ignored in line " + str(lineNum))

    if bAllow == False:
        print("Not enought parameters for replacing in line " + str(lineNum)+ ", skip")
    else:       
        #print(textFind, textReplace)
        # Replacement
        filedata = filedata.replace(textFind,textReplace)

if len(replaces) > len(set(replaces)):
    result = Mbox('Data duplication', 'Some "Replace words" are not unique that might be a mistake. Confirm replacement?', MB_OKCANCEL)
    if result == IDCANCEL:
        sys.exit()
        
f = open(fileOut,'w')
f.write(filedata)
f.close()   
