def readfile(filename):
    directions=[]
    with open(filename) as f:
        for line in f:
            directions.append(line[:line.index('(')-1].split(' '))
    return directions

def nextStep(coord, step):
    if step =='U':
        return (coord[0],coord[1]+1)
    elif step =='D':
        return (coord[0],coord[1]-1)
    elif step == 'L':
        return (coord[0]-1,coord[1])
    elif step =='R':
        return (coord[0]+1,coord[1])



def tracePath(directions):
    pathDict={}
    currentCoord=(0,0)
    maxY=-1
    maxX=-1
    for step in directions:
        for i in range(int(step[1])):

            pathDict[currentCoord]=nextStep(currentCoord,step[0])
            currentCoord=pathDict[currentCoord]
            if currentCoord[0]>maxX:
                maxX=currentCoord[0]
            if currentCoord[1]>maxY:
                maxY=currentCoord[1]
    return pathDict, maxX, maxY






""" from day 10"""


def recorddirections(pathMap):
    firstChar=(0,0)
    secondChar=pathMap[firstChar]
    pathlist={}
    i=1
    while secondChar!=(0,0):
        if firstChar not in pathlist:
            pathlist[firstChar]=[(secondChar[0]-firstChar[0],secondChar[1]-firstChar[1])]
        if secondChar not in pathlist:
            pathlist[secondChar]=[(secondChar[0]-firstChar[0],secondChar[1]-firstChar[1])]
        firstChar=secondChar
        secondChar = pathMap[firstChar]
        pathlist[firstChar].append((secondChar[0]-firstChar[0],secondChar[1]-firstChar[1]))
    return pathlist

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
        #print("here", pathcopy)
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


""""""

def mainfunction(filename):
    directions=readfile(filename)
    pathDict, maxX, maxY = tracePath(directions)
    pathdirections=recorddirections(pathDict)
    enclosedDict=repeatRight(pathdirections, maxX, maxY)
    return len(enclosedDict)

print(mainfunction('input18.txt'))
