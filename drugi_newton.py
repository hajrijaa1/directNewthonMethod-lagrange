import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def newtonova(x, y, xi):
    #dužina unesenih tačaka
    n = len(x)
    #inicijalizacija podjeljene razlike
    fdd = [[None for x in range(n)] for x in range(n)]
    # vrijednost f(X) na različitim koracima
    yint = [None for x in range(n)]
    #error vrijednost
    ea = [None for x in range(n)]
    
    # Pronalaženje podijeljenje razlike
    for i in range(n):
        fdd[i][0] = y[i]
    for j in range(1,n):
        for i in range(n-j):
            fdd[i][j] = (fdd[i+1][j-1] - fdd[i][j-1])/(x[i+j]-x[i])
    
    # ispisivanje u tebalu
    fdd_table = pd.DataFrame(fdd)
    print(fdd_table)
    
    # interpolacija x
    xterm = 1
    yint[0] = fdd[0][0]
    for order in range(1, n):
        xterm = xterm * (xi - x[order-1])
        yint2 = yint[order-1] + fdd[0][order]*xterm
        ea[order-1] = yint2 - yint[order-1]
        yint[order] = yint2
    
    # vraćanje karte za pandas dataframe 
    return map(lambda yy, ee : [yy, ee], yint, ea)

# Upisivanje traženih vrijednosti
#Unošenje broja nepoznatih 
n = int(input("Unesite broj nepoznatih: "))
#Izrada numpy niza veličine n*n za pohranu unesenih vrijednosti
x = np.zeros((n))
y = np.zeros((n))

#Unos vrijednosti:
for i in range(n):
    x[i]=float(input("x [" + str(i) + "]: "))
    y[i]=float(input("y [" + str(i) + "]: "))


# Pozivanje funkcije
a = newtonova(x, y, 2)
df = pd.DataFrame(a, columns=['f(x)','error'])