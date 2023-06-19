from xml.etree.ElementPath import xpath_tokenizer
import numpy as np
import sys

#Unošenje broja nepoznatih 
n = int(input("Unesite broj nepoznatih: "))

#Izrada numpy niza za pohranu unesene matrice
a = np.zeros((n,n+1))
#Izrada numpy niza za pohranu rješenja
x = np.zeros(n)

#Upisivanje elemenata matrice
#Počinje od a[0,0] i zaustavlja se na a[n, n+1]
print("Unesite koeficijente matrice: ")
for i in range(n):
    for j in range(n+1):
        a[i][j] = float(input( 'a['+str(i)+']['+ str(j)+']='))

#Primjena Gauss Jordanove metode eliminacije
#Postavljamo uslov da je nemoguće dijeljene s nulom, pri čemu će se ispisati odgovarajuća poruka.
for i in range(n):
    if a[i][i] == 0.0:
        sys.exit("ERROR! Dijeljene s 0 nemoguće!")
        
    #Postavljamo uslov gdje je i različit od j
    for j in range(n):
        if i != j:
            faktor = a[j][i]/a[i][i]

            for k in range(n+1):
                a[j][k] = a[j][k] - faktor * a[i][k]
#Na kraju, dobivamo rješenje:
for i in range(n):
    x[i] = a[i][n]/a[i][i]

#Unos vrijednosti koja se traži za interpolaciju polinoma
xp = float(input("Unesite vrijednost za interpolaciju: "))
#Ispisivanje rješenja Gauss Jordanove metode
print("Traženo rješenje je: ")
for i in range(n):
    print('X%d = %0.6f' %(i,x[i]), end = '\t')

#Ako korisnik unese vrijednost 2 za interpolaciju, ispisuje mu se rješenje 
# za linearni polinom, analogno za kvadratni i kubni polinom.
if n == 2:
    #P označava funkciju polinoma
    #Prethodno izračunata rješenja Gaussovom metodom se 
    # uzimaju u oznakama x[i-3],x[i-2],x[i-1] i x[i]
    # u zavisnosti od stepena polinoma   
    P = x[i-1] + (x[i]*xp)
    print("\nRješenje linearnog polinoma je: %.6f. " % (P))
if n == 3:
    P = (x[i-2]) + (x[i-1]*xp) + (x[i]*(pow(xp,2)))
    print("\nRješenje kvadratnog polinoma je: %.6f. " % (P))
if n == 4:
    P = (x[i-3]) + (x[i-2]*xp) + (x[i-1]*(pow(xp,2))) + (x[i]*(pow(xp,3)))
    print("\nRješenje kubnog polinoma je: %.6f. " % (P))
