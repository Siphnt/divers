import math #on importe pi

def disque(r):
   y=math.pi*r**2 #on fait le calcul  
   return y #on retourne a y

def rectangle(larg,long):
    z=larg*long
    return z 

def triangle(n):
    a="O "
    b="O "
    for i in range(n):
        print(a)
        a=a+b

def moities(j):
    while (j>1):
                j=j/2
                print(j)
    return j

def paires_num(m) :
    for i in range(m+1):
        for k in range(m+1):
            print(i,k)

def paires_ordo(m) :
    for i in range(m+1):
        for k in range(i,m+1):
            print (i,k)
