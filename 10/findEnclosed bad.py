def readFile2(filename):
    pipes={}
    startPipe=[]
    maxY=0
    maxX=0
    maxPipex=[]
    #pipeDef={'|':[(x,y-1),(x,y+1)],'-':[(x-1,y),(x+1,y)],'L':[(x,y-1),(x+1,y)],'J':[(x,y-1),(x-1,y)],'7':[(x-1,y),(x,y+1)],'F':[(x+1,y),(x,y+1)]}
    with open(filename) as f:
        for y, line in enumerate(f):
            maxPipex.append(-1)
            for x, s in enumerate(line):
                if s in {'|':[(x,y-1),(x,y+1)],'-':[(x-1,y),(x+1,y)],'L':[(x,y-1),(x+1,y)],'J':[(x,y-1),(x-1,y)],'7':[(x-1,y),(x,y+1)],'F':[(x+1,y),(x,y+1)]}:
                    pipes[(x,y)]={'|':[(x,y-1),(x,y+1)],'-':[(x-1,y),(x+1,y)],'L':[(x,y-1),(x+1,y)],'J':[(x,y-1),(x-1,y)],'7':[(x-1,y),(x,y+1)],'F':[(x+1,y),(x,y+1)]}[s]
                    if x>maxPipex[y]:
                        maxPipex[y]=x
                    if startPipe!={}:
                        if pipes[(x,y)][0] in startPipe:
                            startPipe.append((x,y))
                        elif pipes[(x,y)][1] in startPipe:
                            startPipe.append((x,y))
                if s=='S':
                    startPipe.append((x,y))
                if x>maxX:
                    maxX=x
            if y>maxY:
                maxY=y
        maxY+=1
        maxX

    return startPipe,pipes,maxY, maxX, maxPipex



#too deep of a recursion
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

"""
def mainFunction(filename):
    start,pipeMap=readFile(filename)
    firstChar=start[0]
    secondChar=start[1]
    pipeMap[firstChar]=[secondChar,0]
    print(pipeMap)
    i=1
    while secondChar!=start[0]:
        firstChar,secondChar = getNextChar(pipeMap,firstChar,secondChar)
        i+=1
    return i
"""

    #return followPath(pipeMap, firstChar, secondChar,firstChar,0)

#couldnt get this to work due to multiple pipes in a row
def countEnclosed(pipeMap,height,width,maxPipex):
    pipeList=[]
    enclosedCount=0
    for pipe in pipeMap:
        pipeList.append(pipe)

    #for coord in pipeList:
    #    if len(pipeList)<(coord[1]+1)
    for y in range(height):
        i=0
        for x in range(width):
            if (x,y) in pipeList:
                i+=1

            elif i%2==1 and i!=0 and x<maxPipex[y]:
                enclosedCount+=1
                print(x,y)
    return enclosedCount






def mainFunction2(filename):
    start,pipeMap,numRows,numColumns,maxPipex=readFile2(filename)
    print(numRows)
    print(numColumns)
    pipeMap[start[0]]=[start[1],0]
    pipeCoords=countEnclosed(pipeMap,numRows,numColumns,maxPipex)
    return pipeCoords

print(mainFunction2('inputtest2.txt'))
