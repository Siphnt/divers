import random

def elimine(truc):
    rep=[]
    for valeur in truc:
        if valeur not in rep:
            rep.append(valeur)
    return rep

def carte(n):
    nb=['7 ','8 ','9 ','10 ','valet ','dame ','roi ','as ']
    couleur=['de trefle','de pique','de coeur','de carreau']
    main=[]
    while n>len(main):
        a=random.choice(nb) + random.choice(couleur)
        if a not in main :
            main.append(a)
    return main

def mains_et_pioche(n):
    pioche = carte(32)
    main1=[]
    main2=[]
    while n>len(main1) and n>len(main2):
        a=random.choice(pioche)
        b=random.choice(pioche)
        main1.append(a)
        main2.append(b)
        pioche.remove(a)
        pioche.remove(b)
    return pioche , main1 , main2

def nieme(L,n):
    rep=''
    c=0
    for i in L:
        if len(L[c])<n:
            return 'mettre un nombre inférieur a ' + str(len(L[c]))
        c=c+1
    for a in L:
        rep=rep+a[n-1]
    return rep

def extremin(l):
    mi=l[0]
    for item in range(len(l)):
        if mi>l[item]:
            mi=l[item]
    return mi
def tri_sel(l):
    l2=[]
    while len(l)>0:
        l2.append(extremin(l))
        l.remove(extremin(l))
    return l2

def tri_ins(l):
    l2=[l[0]] 
    for terme in l[1:]:       
        i=len(l2)
        while terme<l2[i-1] and i>0:
            i=i-1
        l2.insert(i, terme)
    return l2
    