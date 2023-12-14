def readFile(filename):
    cuberocks=[]
    circlerocks=[]
    sumtotal=0
    with open(filename) as f:
        for i, line in enumerate(f):
            for j,s in enumerate(line[:line.index('\n')]):
                if len(cuberocks)<=j:
                    cuberocks.append([])
                if len(circlerocks)<=j:
                    circlerocks.append([])
                if s == '#':
                    cuberocks[j].append(i)
                if s =='O':
                    if circlerocks[j]==[]:
                        cmax=-1
                    else:
                        cmax=max(circlerocks[j])
                    if cuberocks[j]==[]:
                        rmax=-1
                    else:
                        rmax=max(cuberocks[j])
                    circlerocks[j].append(max(rmax,cmax)+1)
                    sumtotal+=(100-circlerocks[j][-1])





    return circlerocks, sumtotal


"""
    def west(circles,cubes):

    for x in range(len((circles)):
        for y in range(len(circles[x])):
            if circlerocks[x]==[]:
                        cmax=-1
                    else:
                        cmax=max(circlerocks[j])
                    if cuberocks[j]==[]:
                        rmax=-1
                    else:
                        rmax=max(cuberocks[j])
"""



print(readFile('input14.txt'))
