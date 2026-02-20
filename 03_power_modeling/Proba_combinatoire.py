import numpy as np
mon_dict = {"T1": 10, "T2": 5, "T3": 60, "T4": 20,"T5": 22, "T6":90, "T7":11, "T8":51  }

# Taches, valeur = mon_dict.items()
# for i in valeur:
#     print(valeur)
import copy
Taches = ["T1","T2","T3","T4","T5","T6","T7","T8"]
n = 4
def combin(n, k):
    """Nombre de combinaisons de n objets pris k a k (non récursif, mais imitant le récursif)"""
    pile = [[n,k]]
    r = 0
    print (r, pile)
    while len(pile)>0:
        i, j = pile.pop(-1)
        if j==0 or i==j:
            r += 1
            print (r, pile)
        else:
            
            pile.append([i-1,j-1])
            pile.append([i-1,j])
            print (r, pile)
    return r


def combinliste(seq, k):
    p = []
    i, imax = 0, 2**len(seq)-1
    while i<=imax:
        s = []
        j, jmax = 0, len(seq)-1
        while j<=jmax:
            if (i>>j)&1==1:
                s.append(seq[j])
            j += 1
        if len(s)==k:
            p.append(s)
        i += 1 
    return p


p = combinliste(Taches,n)
print(combinliste(Taches,n))


C = combinliste(Taches,n)
i=0
while i < len(C):
    C[i] = copy.deepcopy(Taches)
    i = i+1
    
r = combinliste(Taches,n)

for j in range(len(C)):
    r[j] = list(set(C[j]) - set(C[j]).intersection(set(p[j])))
    
NewL = copy.deepcopy(p)

for d in range (len(p)):
    for s in range(n):
        NewL[d][s] = p[d][s],r[d][s]
    
# for d in range (len(p)):
#     for s in range(n):
#         for u in range(n):
#             print(NewL[d][s][u])

def charge(x,n):
    charge1C = np.zeros((x,n))
    for d in range (x):
        for s in range(n):
             for u in range(2):
                 charge1C[d][s] =  charge1C[d][s] + mon_dict[NewL[d][s][u]]
    return charge1C    
    
chargeC = charge(len(p),n)
lineR,columnR = np.where(chargeC > 100) 
print("Nous avons rejeté distribution:")
print(len(columnR))

    
            

    



