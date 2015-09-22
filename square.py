import numpy as np
import matplotlib.pyplot as plt
import csv

t  = 1
L  = 8
NB = 99
N2 = L*L 

def neig(i):
    res = [None] * 4

    res[0] = i+1
    if(res[0]%L == 1):
        res[0]=i+1-L
    
    res[1] = i-1
    if(res[1]%L == 0):
        res[1]=i-1+L
    
    res[2] = i+L
    if(res[2] >= N2):
        res[2]=(i+L-N2)%N2

    res[3] = i-L
    if(res[3] <= 0): 
        res[3]=(i-L+N2)

    return res

def perFac(i,j,B):
    n = neig(i)
    if i>j:
        if j==n[0]:
            return np.exp(  1j * B * 2 * np.pi )
        elif j==n[1]:
            return np.exp( -1j * B * 2 * np.pi )
        elif j==n[2]:
            return np.exp(  1j * B * 2 * np.pi )
        elif j==n[3]:
            return np.exp(  -1j * B * 2 * np.pi )
        else:
            return 1
    else:
        if j==n[0]:
            return np.exp( -1j * B * 2 * np.pi )
        elif j==n[1]:
            return np.exp(  1j * B * 2 * np.pi )
        elif j==n[2]:
            return np.exp( -1j * B * 2 * np.pi )
        elif j==n[3]:
            return np.exp(  1j * B * 2 * np.pi )
        else:
            return 1
H = [[0 for i in range(N2)] for i in range(N2)] 

def tij(x,y,B):
    return [[ (perFac(x,y,B) if (i==x and j==y) else 0)  for i in range(N2)] for j in range(N2)] 

with open(str(L)+'x'+str(L)+str(NB) +'.csv', 'wt') as csvfile:
    output = csv.writer(csvfile, delimiter=',',quotechar=' ', quoting=csv.QUOTE_MINIMAL)

    for B in np.linspace(0,1,NB):
        H = [[0 for i in range(N2)] for i in range(N2)] 
        for i in range(1,N2+1):
            for j in range(0,4,1):
                H = np.add(H, tij(i-1,neig(i)[j]-1,B) )

        output.writerow(np.linalg.eigh(H)[0])
