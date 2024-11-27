from math import sqrt

"""Exercice 1 - Écrire une fonction surf qui
- accepte en paramètres 2 tuples de deux termes qui seront les coordonnées de deux points dans un plan 
- renvoie la surface du rectangle dont les deux points sont les coins opposés."""

def surf(a,b):
    (xa,ya)=a
    (xb,yb)=b
    aire=abs((xb-xa)*(yb-ya))
    return aire

"""Exercice 2 - Écrire une fonction racines qui
 - accepte en paramètre un tuple de trois termes qui seront les trois coefficients d'un polynôme du second degré (a,b,c) 
 - renvoie sous forme de tuple ses 2 racines."""

def racine(x):
    delta=(x[1]**2)-(4*x[0]*x[2])
    print(delta)
    if delta<0:
        return "pas de solution"
    elif delta ==0:
        return -x[1]/(2*x[0])
    else:
        return (-x[1]+sqrt(delta))/(2*x[0]), (-x[1]-sqrt(delta))/(2*x[0])
    
def toto(tu):
    for item in range (len(tu)): #parcours par les indinces
        print(item,tu[item])
 
"""Exercice 3 - Écrire une fonction trouve qui
- prend en argument un tuple et un élément
- renvoie la position de cet élément dans le tuple. Elle renverra -1 si l’élément n’est pas trouvé. """      
def trouve(a,b):
    for i in range (len(a)):#parcours les valeurs
        if a[i]==b:
            return i
    return -1
"""Exercice 4 - Écrire une fonction extremes qui
- prend en argument un tuple composé de nombres entiers 
- renvoie un tuple contenant le plus grand des entiers et le plus petit."""
def extremes(a):
    ma=a[0]
    mi=a[0]
    for item in range (len(a)):
        if ma<a[item]:
            ma=a[item]
        elif mi>a[item]:
            mi=a[item]
    return mi,ma
        
"""Exercice 5 - Écrire une fonction separe qui
- prend en argument un tuple composé de nombres entiers 
- renvoie un tuple contenant deux tuples : le premier ne contenant que les entiers pairs du tuple de départ et le deuxième que les entiers impairs.
ATTENTION un p-uplet avec p=1 (exemple chaine 'hello' comme seul terme) doit être codé ('hello',) et non('hello')"""

def separe(a):
    paire=()
    impaire=()
    for item in range (len(a)):
        b=a[item]%2
        if b==0:
            paire = paire + (a[item],)
        else :           
            impaire = impaire + (a[item],)
    return "paire :", paire , "impaire :" ,impaire
        