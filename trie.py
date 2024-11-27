from random import*
import time

"""2 - Individuel :
Coder deux fonctions tri_ins (L) et tri_sel (L) qui admettent  L comme paramètre et retourne L triée dans l'ordre croissant.
L'une sera conforme à un algorithme de tri par insertion, l'autre de tri par sélection.
     naturellement tout recours à un outil python tel que .sort() ou sorted() ou min() est interdit
Tester vos fonctions en soumettant des listes d'entiers aléatoires créées par vos fonctions du cours précédent"""
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
    for i in range(20000):
        p=randint(0,100)
        l.append(p)
    return l