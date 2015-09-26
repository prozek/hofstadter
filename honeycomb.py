import numpy as np
import csv

t  = 1
L  = 3
NB = 49
N2 = 2*L*2*L
tot = 2*L*2*L

def ypos(x):
    rest = x % (2*L)
    return (x-rest)/(2*L)+1

def xpos(x):
    return x % (2*L)

def neig(i):
    res = [None] * 3

    res[0] = i+1
    if (res[0] % (2*L) == 1):
        res[0] -= 2*L

    res[1] = i-1
    if (res[1] % (2*L) == 0):
        res[1] += 2*L

    res[2] = i
    if ( ypos(res[2]) == 1 ):
        if( res[2] % 2 == 0 ):
            res[2] += 2*L*2*L-2*L
        elif( res[2] % 2 == 1):
            res[2] += 2*L
    elif ( ypos(res[2]) == 2*L):
        if( res[2] % 2 == 1):
            res[2] -= 2*L
        elif(res[2] % 2 == 0):
            res[2] -= 2*L*2*L-2*L
    else:
        if(ypos(res[2]) % 2 == 0):
            if (res[2] % 2 == 0):
                res[2] += 2*L
            elif(res[2] % 2 == 1):
                res[2] -= 2*L
        elif(ypos(res[2]) % 2 == 1):
            if (res[2] % 2 == 1):
                res[2] += 2*L
            elif(res[2] % 2 == 0):
                res[2] -= 2*L

    return res

def perFac(i,j,B):
    n = neig(i)[2]
    if(xpos(i) % 2 == 1):
        return np.exp(  1j * B * 2 * np.pi * (xpos(i)-1) )
    elif(xpos(i) % 2 == 0):
        return np.exp(  -1j * B * 2 * np.pi * (xpos(i)-1) )
    else:
        return 1

H = [[0 for i in range(N2)] for i in range(N2)] 

def tij(x,y,B):
    return [[ (perFac(i,j,B) if (i==x and j==y) else 0)  for i in range(N2)] for j in range(N2)] 

#for i in range(1,tot+1):
#    print(str(i)+" ; "+str(neig(i)))

with open(str(L)+'x'+str(L)+str(NB) +'.csv', 'wt') as csvfile:
    output = csv.writer(csvfile, delimiter=',',quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    
    for B in np.linspace(0,1,NB):
        H = [[0 for i in range(N2)] for i in range(N2)] 
        for i in range(1,N2+1):
            for j in range(0,3,1):
                H = np.add(H, tij(i-1,neig(i)[j]-1,B))
        
        output.writerow(np.linalg.eigh(H)[0])
