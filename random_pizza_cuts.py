import numpy as np
import matplotlib.pyplot as plt
import itertools
import fractions

from fractions import Fraction 
from numpy import *

px = []
py = []


def perp( a ) :
    b = empty_like(a)
    b[0] = -a[1]
    b[1] = a[0]
    return b

def seg_intersect(a1,a2, b1,b2) :
    da = a2-a1
    db = b2-b1
    dp = a1-b1
    dap = perp(da)
    denom = dot( dap, db)
    num = dot( dap, dp )
    return (num / denom)*db + b1

def i_to_l(i):
  return {
    0 : 'A',
    1 : 'B',
    2 : 'C',
    3 : 'D',
    4 : 'E',
    5 : 'F',
  }[i]

tries = 0
pieces = {}
pieces[0] = 0
pieces[1] = 0
pieces[2] = 0
pieces[3] = 0

sequence_0 = {}
sequence_1 = {}
sequence_2 = {}
sequence_3 = {}

count = 0

for i in range(1,100000):
    alpha = {}  
    # generate 6 random angles around a circle 
    t = np.random.random_sample(6) * np.pi

    # create a mapping between angles and point identifiers e.g. ABCDEF 
    for i in range(0,len(t)):
         alpha[t[i]] = i_to_l(i)
    t2 = t.copy()
    t2.sort()
    s = ''
    for a in t2:
      s += alpha[a]

    # generate x,y coordintaes from angles
    x = 1 + np.cos(t)
    y = 1 + np.sin(t)

    chord = {}
    chord[1] = []
    chord[2] = []
    chord[3] = []
    tries = tries + 1

    # data strucure for chords
    for w in range(0,int(len(t)/2)):
        j = w*2
        p1 = array( [ x[j], y[j] ] )
        p2 = array( [ x[j+1], y[j+1] ] )
        chord[w+1].append(p1)
        chord[w+1].append(p2)

    # calculate intersects
    # first calculate the intersect of 2 lines and then deermine if intersection
    # point lies within the circle
    intersects = 0
    for h in range(1,4):
        cA = chord[h]
        for f in range(h+1,4):
            #print(str(h)+"->"+str(f))
            cB = chord[f]
            
            m = seg_intersect(cA[0],cA[1],cB[0],cB[1])
            d = np.linalg.norm(m-[1,1])
            if(d < 1):
               intersects = intersects + 1

    # count number of intersections per try
    pieces[intersects] = pieces[intersects] + 1

    # log permutations
    if((intersects == 3) and (s[0] == 'A')):
       if(s in sequence_3.keys()):
         pass
       else:
         sequence_3[s] =1
    if((intersects == 2) and (s[0] == 'A')):
       if(s in sequence_2.keys()):
         pass
       else:
         sequence_2[s] =1
    if((intersects == 1) and (s[0] == 'A')):
       if(s in sequence_1.keys()):
         pass
       else:
         sequence_1[s] =1
    if((intersects == 0) and (s[0] == 'A')):
       if(s in sequence_0.keys()):
         pass
       else:
         sequence_0[s] =1


# results
x = itertools.permutations(['B','C','D','E','F'])
total_perms  = len(list(x))

zero = round((pieces[0]/tries) * 100, 2)
one = round((pieces[1]/tries) * 100, 2)
two = round((pieces[2]/tries) * 100, 2)
three = round((pieces[3]/tries) *100, 2)

print("")
print("ZERO INTERSECTIONS (4 PIECES)")
print("-----------------------------")
print(", ".join(sequence_0.keys()))
noc0 = len(sequence_0.keys())
fnoc0 = Fraction(noc0/total_perms).limit_denominator()
print("")
print("NO. OF CONFIGURATIONS: "+str(noc0)+" TOTAL: "+str(total_perms))
print("PROBABILITY: "+str(fnoc0))
print("SIMULATION P(): "+str(zero)+"%")
print("-----------------------------")

print("ONE INTERSECTIONS (5 PIECES)")
print("-----------------------------")
print(", ".join(sequence_1.keys()))
noc1 = len(sequence_1.keys())
fnoc1 = Fraction(noc1/total_perms).limit_denominator()
print("")
print("NO. OF CONFIGURATIONS: "+str(noc1)+" TOTAL: "+str(total_perms))
print("PROBABILITY: "+str(fnoc1))
print("SIMULATION P(): "+str(one)+"%")
print("-----------------------------")

print("TWO INTERSECTIONS (6 PIECES)")
print("-----------------------------")
print(", ".join(sequence_2.keys()))
noc2 = len(sequence_2.keys())
fnoc2 = Fraction(noc2/total_perms).limit_denominator()
print("")
print("NO. OF CONFIGURATIONS: "+str(noc2)+" TOTAL: "+str(total_perms))
print("PROBABILITY: "+str(fnoc2))
print("SIMULATION P(): "+str(two)+"%")
print("-----------------------------")

print("THREE INTERSECTIONS (7 PIECES)")
print("-----------------------------")
print(", ".join(sequence_3.keys()))
noc3 = len(sequence_3.keys())
fnoc3 = Fraction(noc3/total_perms).limit_denominator()
print("")
print("NO. OF CONFIGURATIONS: "+str(noc3)+" TOTAL: "+str(total_perms))
print("PROBABILITY: "+str(fnoc3))
print("SIMULATION P(): "+str(three)+"%")
print("-----------------------------")
print("")



