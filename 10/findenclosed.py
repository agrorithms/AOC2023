def readFile(filename):
    pipes={}
    startPipe=[]
    maxX=0
    maxY=0
    #pipeDef={'|':[(x,y-1),(x,y+1)],'-':[(x-1,y),(x+1,y)],'L':[(x,y-1),(x+1,y)],'J':[(x,y-1),(x-1,y)],'7':[(x-1,y),(x,y+1)],'F':[(x+1,y),(x,y+1)]}
    with open(filename) as f:
        for y, line in enumerate(f):
            for x, s in enumerate(line):
                if y==1:
                    if x>maxX:
                        maxX=x
                if s in {'|':[(x,y-1),(x,y+1)],'-':[(x-1,y),(x+1,y)],'L':[(x,y-1),(x+1,y)],'J':[(x,y-1),(x-1,y)],'7':[(x-1,y),(x,y+1)],'F':[(x+1,y),(x,y+1)]}:
                    pipes[(x,y)]={'|':[(x,y-1),(x,y+1)],'-':[(x-1,y),(x+1,y)],'L':[(x,y-1),(x+1,y)],'J':[(x,y-1),(x-1,y)],'7':[(x-1,y),(x,y+1)],'F':[(x+1,y),(x,y+1)]}[s]
                    if startPipe!={}:
                        if pipes[(x,y)][0] in startPipe:
                            startPipe.append((x,y))
                        elif pipes[(x,y)][1] in startPipe:
                            startPipe.append((x,y))
                if s=='S':
                    startPipe.append((x,y))
            if y>maxY:
                maxY=y
        maxY+=1
    return startPipe,pipes, maxX, maxY



#too deep of recursion
"""
def followPath(pipeMap,char1,char2,endchar,i):
    i+=1
    lastchar=char2
    if pipeMap[char2][0]==char1:
        nextchar=pipeMap[char2][1]
    elif pipeMap[char2][1]==char1:
        nextchar=pipeMap[char2][0]
    if lastchar!=endchar:
        return followPath(pipeMap,lastchar,nextchar,endchar,i)
    return lastchar,i
"""


def getNextChar(pipeMap,char1,char2):
    lastchar=char2
    if pipeMap[char2][0]==char1:
        nextchar=pipeMap[char2][1]
    elif pipeMap[char2][1]==char1:
        nextchar=pipeMap[char2][0]
    return lastchar,nextchar


def recordPath(pipeMap,char1,char2):
    firstChar=char1
    secondChar=char2
    pathlist={}
    i=1
    while secondChar!=char1:
        if firstChar not in pathlist:
            pathlist[firstChar]=[(secondChar[0]-firstChar[0],secondChar[1]-firstChar[1])]
        if secondChar not in pathlist:
            pathlist[secondChar]=[(secondChar[0]-firstChar[0],secondChar[1]-firstChar[1])]
        firstChar,secondChar = getNextChar(pipeMap,firstChar,secondChar)
        pathlist[firstChar].append((secondChar[0]-firstChar[0],secondChar[1]-firstChar[1]))

        i+=1
    return i/2, pathlist

def rightHand(pathDict, maxX, maxY):
    enclosedDict=pathDict.copy()
    for pipe in pathDict:
        for i in range(len(pathDict[pipe])):
            if (pipe[0]-pathDict[pipe][i][1],pipe[1]+pathDict[pipe][i][0]) not in pathDict:
                if (pipe[0]-pathDict[pipe][i][1])>maxX or (pipe[1]+pathDict[pipe][i][0])>maxY:
                    print("right",pipe[0]-pathDict[pipe][i][1],pipe[1]+pathDict[pipe][i][0])
                    return False, False

                enclosedDict[(pipe[0]-pathDict[pipe][i][1],pipe[1]+pathDict[pipe][i][0])]=pathDict[pipe]
    return enclosedDict, len(enclosedDict)


def leftHand(pathDict, maxX, maxY):
    enclosedDict=pathDict.copy()
    for pipe in pathDict:
        for i in range(len(pathDict[pipe])):
            if (pipe[0]+pathDict[pipe][i][1],pipe[1]-pathDict[pipe][i][0]) not in pathDict:
                if (pipe[0]+pathDict[pipe][i][1])>maxX or (pipe[1]-pathDict[pipe][i][0])>maxY:
                    print("left",(pipe[0]+pathDict[pipe][i][1],pipe[1]-pathDict[pipe][i][0]))
                    return False, False

                enclosedDict[(pipe[0]+pathDict[pipe][i][1],pipe[1]-pathDict[pipe][i][0])]=pathDict[pipe]
    return enclosedDict, len(enclosedDict)

def repeatRight(pathDict, maxX, maxY):
    pathcopy=pathDict.copy()
    len0=len(pathcopy)
    len1=len(pathcopy)
    len2=1
    while len1!=len2 and len2:
        if len2!=1:
            len1=len2
        pathcopy, len2 = rightHand(pathcopy, maxX, maxY)
        #print(len2)
    if len2==False:
        pathcopy=pathDict.copy()
        print("here", pathcopy)
        len0=len(pathcopy)
        len1=len(pathcopy)
        len2=0
        while len1!=len2:
            if len2!=0:
                len1=len2
            pathcopy, len2 = leftHand(pathcopy,maxX,maxY)




    return pathcopy


def getnewdict(enclosedcopy, pathDict):
    for key in pathDict:
        del enclosedcopy[key]

    return enclosedcopy


def mainFunction(filename):
    start,pipeMap,maxX, maxY=readFile(filename)
    firstChar=start[0]
    secondChar=start[1]
    pipeMap[firstChar]=[secondChar,0]
    farthestpipe, pathDict = recordPath(pipeMap,firstChar, secondChar)
    print("og len pathdict",len(pathDict))
    enclosed = repeatRight(pathDict, maxX, maxY)

    onlyenclosed=getnewdict(enclosed,pathDict)
    """
    pathlist={}
    pathlist[firstChar]=(secondChar[0]-firstChar[0],secondChar[1]-firstChar[1])
    i=1
    while secondChar!=start[0]:
        firstChar,secondChar = getNextChar(pipeMap,firstChar,secondChar)
        pathlist[firstChar](secondChar[0]-firstChar[0],secondChar[1]-firstChar[1])

        i+=1
    return i
    """
    return len(onlyenclosed)

    #return followPath(pipeMap, firstChar, secondChar,firstChar,0)


print(mainFunction('input10.txt'))
