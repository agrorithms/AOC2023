def readFile(filename):
    rocklist=[]
    columntotallist=[]
    rowtotal=0
    linecount=[]
    bigcolumnlist=[]
    columntotal=0
    group=0
    with open(filename) as f:
        for y, line in enumerate(f):
            if line =='\n':
                #print(rowtotal)
                r=checkMirror(rocklist)
                rowtotal+=r
                rocklist=[]
                group+=1
                if r!=0:
                    linecount.append(group)

                if columntotallist[0]!=[]:
                    if len(columntotallist[0])!=1:
                        print(y, columntotallist)
                    columntotal+=columntotallist[0][0]
                    linecount.append(group)
                columntotallist=[]
            #for s in line[:line.index('\n')]
            #    columntotal+=checkMirror()

            else:
                rocklist.append(line[:line.index('\n')])
                newmirror=checkMirror(line[:line.index('\n')])
                if columntotallist==[]:
                    columntotallist.append(newmirror)
                else:
                    columntotallist.append([])
                    for num in newmirror:
                        if num in columntotallist[0]:
                            columntotallist[1].append(num)
                    columntotallist.pop(0)


                #columntotallist.append(checkMirror(line[:line.index('\n')]))
                #elif check
        rowtotal+=checkMirror(rocklist)
        if columntotallist[0]!=[]:
                    if len(columntotallist[0])!=1:
                        print(y, columntotallist)
                    columntotal+=columntotallist[0][0]
    return rowtotal*100, columntotal, rowtotal*100+columntotal, group, len(linecount)



def checkMirror(rocklist):
    rowtotal=0
    stringlist=[]
    for i, row in enumerate(rocklist):
        if i>0 and i !=(len(rocklist)):
            d = min(i,len(rocklist)-i)


            if rocklist[i-d:i]== rocklist[::-1][-i-d:-i]:
                print(i-d,i, -i-d,-i)
                if isinstance(rocklist,str):
                    stringlist.append(i)
                rowtotal+=i

    if isinstance(rocklist,str):
        print(stringlist)
        print(rocklist)
        return stringlist
    return rowtotal



print(readFile('input13.txt'))
print((isinstance('p',str)))
