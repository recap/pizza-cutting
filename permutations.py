import itertools

x = itertools.permutations(['B','C','D','E','F'])
lx = list(x)
counter = 0
for i in range(0,len(lx)):
    print("A" + str(lx[i][0])+str(lx[i][1]) + str(lx[i][2]) + str(lx[i][3]) + str(lx[i][4]) )
    counter += 1

print("total permustations: "+str(counter))

