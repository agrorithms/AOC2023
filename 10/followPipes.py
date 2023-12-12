def readFile(filename):
    pipes={}
    startPipe=[]
    #pipeDef={'|':[(x,y-1),(x,y+1)],'-':[(x-1,y),(x+1,y)],'L':[(x,y-1),(x+1,y)],'J':[(x,y-1),(x-1,y)],'7':[(x-1,y),(x,y+1)],'F':[(x+1,y),(x,y+1)]}
    with open(filename) as f:
        for y, line in enumerate(f):
            for x, s in enumerate(line):
                if s in {'|':[(x,y-1),(x,y+1)],'-':[(x-1,y),(x+1,y)],'L':[(x,y-1),(x+1,y)],'J':[(x,y-1),(x-1,y)],'7':[(x-1,y),(x,y+1)],'F':[(x+1,y),(x,y+1)]}:
                    pipes[(x,y)]={'|':[(x,y-1),(x,y+1)],'-':[(x-1,y),(x+1,y)],'L':[(x,y-1),(x+1,y)],'J':[(x,y-1),(x-1,y)],'7':[(x-1,y),(x,y+1)],'F':[(x+1,y),(x,y+1)]}[s]
                    if startPipe!={}:
                        if pipes[(x,y)][0] in startPipe:
                            startPipe.append((x,y))
                        elif pipes[(x,y)][1] in startPipe:
                            startPipe.append((x,y))
                if s=='S':
                    startPipe.append((x,y))
    return startPipe,pipes




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


def getNextChar(pipeMap,char1,char2):
    lastchar=char2
    if pipeMap[char2][0]==char1:
        nextchar=pipeMap[char2][1]
    elif pipeMap[char2][1]==char1:
        nextchar=pipeMap[char2][0]
    return lastchar,nextchar

def mainFunction(filename):
    start,pipeMap=readFile(filename)
    firstChar=start[0]
    secondChar=start[1]
    pipeMap[firstChar]=[secondChar,0]
    #endchar=(-1,-1)
    i=1
    while secondChar!=start[0]:
        firstChar,secondChar = getNextChar(pipeMap,firstChar,secondChar)
        i+=1
    return i


    #return followPath(pipeMap, firstChar, secondChar,firstChar,0)


print(mainFunction('input10.txt')/2)
