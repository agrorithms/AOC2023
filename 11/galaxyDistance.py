def readfile(filename):
    galaxyList=[]
    noGalaxyColumn=[]
    noGalaxyRow=[]
    with open(filename) as f:

        for y, line in enumerate(f):
            noGalaxyRow.append(True)
            for x, s in enumerate(line):
                if y==0 and s!='\n':
                    noGalaxyColumn.append(True)
                if s =='#':
                    galaxyList.append([x,y])
                    noGalaxyColumn[x]=False
                    noGalaxyRow[y]=False
    return galaxyList,noGalaxyColumn, noGalaxyRow


def addExpansion(galaxyList,noGalaxyColumns,noGalaxyRows):
    for galaxy in galaxyList:
        galaxy[0]+=noGalaxyColumns[:galaxy[0]].count(True)
        galaxy[1]+=noGalaxyRows[:galaxy[1]].count(True)

    return galaxyList

def calcDistances(expandedGalaxyList):
    sumDistance=0
    for i, galaxy in enumerate(expandedGalaxyList):
        for galaxy2 in expandedGalaxyList[i:]:
            sumDistance+=abs(galaxy[0]-galaxy2[0])+abs(galaxy[1]-galaxy2[1])
    return sumDistance



def mainFunction(filename):
    galaxies, doubleColumn, doubleRow=readfile(filename)
    #print (doubleColumn)
    #print(doubleRow)
    expandedGalaxies=addExpansion(galaxies,doubleColumn,doubleRow)
    distance = calcDistances(expandedGalaxies)
    return distance


print(mainFunction('input11.txt'))
