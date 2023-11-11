

#Initial data input
file = open('input.txt', "r")
stringsFromFile = file.readlines()
file.close()

#making the data more usabale for me.
whatToDisappear = [" ",".",",","?","!","(",")",'"',"'","\n"]
for x in range(len(stringsFromFile)):
    for y in range(len(whatToDisappear)):
        stringsFromFile[x] = stringsFromFile[x].replace(whatToDisappear[y],"")
    stringsFromFile[x] = list(stringsFromFile[x].lower())

#testing for palindromes and creating the output array
printoutData = []
for x in range(len(stringsFromFile)):
    length = len(stringsFromFile[x])
    if length%2 == 0:
        charsInString = []
        logical = True
        for y in range(int(length/2)):
            if stringsFromFile[x][y] == stringsFromFile[x][length-1-y]:
                if stringsFromFile[x][y] not in charsInString:
                    charsInString.append(stringsFromFile[x][y])
            else:
                logical = False
                break
        if logical == True:
            printoutData.append("Yes, "+str(len(charsInString)))
        else:
            printoutData.append("No, -1")
    else:
        steps = int((length/2)+0.5)
        charsInString = []
        logical = True
        for y in range(steps):
            if stringsFromFile[x][y] == stringsFromFile[x][length-1-y]:
                if stringsFromFile[x][y] not in charsInString:
                    charsInString.append(stringsFromFile[x][y])
            else:
                logical = False
                break
        if logical == True:
            printoutData.append("Yes, "+str(len(charsInString)))
        else:
            printoutData.append("No, -1")

#printing the output array
for x in printoutData:
    print(x)
