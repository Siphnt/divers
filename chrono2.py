from random import*
import time

"""A - Vous devez d'abord coder une fonction shuff_2pc(L) qui va déplacer 2% des termes pris aux hasard dans une assez grande liste (plus de 100 termes). On la fera travailler pour désordonner faiblement une liste déjà triée
      l'idée est d'en intervertir 2 à chaque fois en
        - tirant au sort deux indices ind1 et ind2 de cette liste
        - intervertir les valeurs entre ces deux rang L[ind1] , L[ind2] = L[ind2] , L[ind1]"""


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

def tirage():
    l=[]
    for i in range(50000):
        p=randint(0,100)
        l.append(p)
    return l
     
def shuff_2pc(l):
    c=len(l)
    for _ in range(len(l)//100):
        a=randint(0, c-1)
        b=randint(0, c-1)
        l[a],l[b]=l[b],l[a]
    a=0
    b=0
    for terme in l:
        if a==c-1:
            return b
        if terme>l[a+1]:
            b=b+1
        a=a+1
    return l

"""B - Maintenant que vous êtes capables d'élaborer des listes 'faiblement désordonnées' et de longueur variable vous allez : 
Lancer deux tris sur des liste 'faiblement désordonnée' l'un par insertion, l'autre par sélection, le tout en le chronométrant chacune de des deux opérations. 
ATTENTION si votre tri est destructif de la liste initiale, vous aurez pris soin d'avoir deux exemplaires identiques de la liste 'faiblement désordonnée' afin de comparer les performance sur deux listes parfaitement identiques.

Multipliez les expériences sur des listes de plus en plus longues pour démontrer que dans ces conditions un des deux algorithmes (insertion ou sélection) se révèle bien plus performant (rapide) que l'autre.
Dites lequel des deux algorithmes profite de la facilité liée au 'meilleur cas'"""




l=tri_ins(tirage())

TOPdebut=time.time()

toto=tri_sel(shuff_2pc(l))

TOPfin=time.time()

duree=TOPfin-TOPdebut



print ('durée pour effectuer le programme',duree)