import numpy as np
import math

#Unošenje broja nepoznatih 
n = int(input("Unesite broj nepoznatih: "))
#Izrada numpy niza veličine n*n za pohranu unesenih vrijednosti
x = np.zeros((n))
y = np.zeros((n))

#Unos vrijednosti:
for i in range(n):
    x[i]=float(input("x [" + str(i) + "]: "))
    y[i]=float(input("y [" + str(i) + "]: "))

#Unos vrijednosti koja se traži za interpolaciju polinoma
xp = float(input("Unesite vrijednost za interpolaciju: "))
#Za yp postavljamo interpoliranu vrijednost na 0
yp = 0

#Formula Lagrangeve interpolacijske funkcije:
for i in range(n):
    p = 1
    for j in range(n):
        if i != j:
            #P predstavlja funkciju polinoma koju računamo
            # xp predstavlja traženu vrijednost za interpolaciju
            # x[j] predstavlja b
            # x[i] predstavlja a, te sve množimo sa f(a)
            p = p * (xp - x[j])/(x[i] - x[j])
    yp = yp + p * y[i]

print("Rješenje interpolacije je %.6f."%(yp))   