def readfile2(filename):
    directions=[]
    with open(filename) as f:
        for line in f:
            directions.append([line[line.index(')')-1],int(line[line.index('(')+2:line.index(')')-1],16)])
    #print(directions)
    return directions


def gatherCorners(directions):
  coordinates=[0+0j]
  area=0
  for i in directions:
      area+=i[1]/2
      if i[0]=='0':
          coordinates.append(coordinates[-1]+i[1])
          area+=.5*(coordinates[-1].real -coordinates[-2].real)*(coordinates[-1].imag+coordinates[-2].imag)
      elif i[0]=='1':
          coordinates.append(coordinates[-1]-i[1]*1j)
      elif i[0]=='2':
          coordinates.append(coordinates[-1]-i[1])
          area+=.5*(coordinates[-1].real -coordinates[-2].real)*(coordinates[-1].imag+coordinates[-2].imag)
      elif i[0]=='3':
          coordinates.append(coordinates[-1]+i[1]*1j)
  #print(coordinates)
  #area+=.5*(coordinates[0].real-coordinates[-1].real)*(coordinates[0].imag+coordinates[0].imag)
  return area+1





def nextStep2(coord, step):
    if step =='U' or step =='3':
        return (coord[0],coord[1]+1)
    elif step =='D' or step == '1':
        return (coord[0],coord[1]-1)
    elif step == 'L' or step == '2':
        return (coord[0]-1,coord[1])
    elif step =='R' or step == '0':
        return (coord[0]+1,coord[1])



def tracePath2(directions):
    pathDict={}
    currentCoord=(0,0)
    maxY=-1
    maxX=-1
    for step in directions:
        for i in range(int(step[1],16)):

            pathDict[currentCoord]=nextStep2(currentCoord,step[0])
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
        dir2=(secondChar[0]-firstChar[0],secondChar[1]-firstChar[1])
        if dir2 not in pathlist[firstChar]:
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



""""""

def mainfunction(filename):
    directions=readfile2(filename)
    #pathDict, maxX, maxY = tracePath2(directions)
    #pathdirections=recorddirections(pathDict)
    #enclosedDict=repeatRight(pathdirections, maxX, maxY)
    enclosedArea=gatherCorners(directions)
    return enclosedArea
print(mainfunction('input18.txt'))
print(mainfunction('inputtest.txt')-952408144115)
#print(int('70c71',16))

#a=1+2j
#b=4


#print(a + b*1j)
