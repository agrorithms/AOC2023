def readfile(filename):
    with open(filename) as f:
        for line in f:
            s=line[:line.index('\n')].split(',')
    return s

def readstep(sequencelist):
    stepList=[]
    for i in sequencelist:
        if i.count('=')==1:
            stepList.append([i[:i.index('=')],int(i[i.index('=')+1:])])
        elif i.count('-')==1:
            stepList.append([i[:i.index('-')],'-'])
    return stepList


def hashstring(string):
            currentvalue=0
            sum=0
            for s in string:
                if s==',':
                    sum+=currentvalue
                    print(currentvalue,sum)
                    currentvalue=0
                elif s=='\n':
                     sum+=currentvalue
                else:
                    currentvalue+=ord(s)
                    #print(currentvalue)
                    currentvalue*=17
                    currentvalue%=256
            sum+=currentvalue
            print(sum)
            return currentvalue


def assignbox(steplist):
    boxDict={}
    for step in steplist:
        boxnum=hashstring(step[0])
        if step[1]!='-':
            if boxnum not in boxDict:
                boxDict[boxnum]=[step]
            else:
                replaced=False
                for i, lens in enumerate(boxDict[boxnum]):
                    if lens[0]==step[0]:
                        boxDict[boxnum][i][1]=step[1]
                        replaced=True
                if replaced==False:
                    boxDict[boxnum].append(step)
        elif step[1]=='-':
            if boxnum in boxDict:

                for i, lens in enumerate(boxDict[boxnum]):
                    if lens[0]==step[0]:
                        boxDict[boxnum].pop(i)
    return boxDict


def calcSum(boxDict):
    sum=0
    for box in boxDict:
        for i, lens in enumerate(boxDict[box]):
            sum+=(box+1)*(i+1)*lens[1]
    return sum




def main(filename):
    stepList=readstep(readfile(filename))
    boxDict = assignbox(stepList)
    sum=calcSum(boxDict)


    return sum


print(readfile('inputtest.txt'))
print(main('input15.txt'))
#print(hashstring('pc'))
#print(ord('q'))
