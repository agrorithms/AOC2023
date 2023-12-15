def readfile(filename):
    currentvalue=0
    sum=0
    with open(filename) as f:
        for line in f:
            #print(line)
            for s in line[:-1]:
                if s==',':
                    sum+=currentvalue
                    print(currentvalue,sum)
                    currentvalue=0
                else:
                    currentvalue+=ord(s)
                    #print(currentvalue)
                    currentvalue*=17
                    currentvalue%=256
            sum+=currentvalue
        print(sum)


readfile('input15.txt')
