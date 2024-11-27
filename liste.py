from random import*
"""A1 Écrire une fonction tirage() qui crée une liste de trente entiers tirés au sort entre 0 et 20 (contient return).
Remarque : il faudra utiliser le module python random"""
def tirage():
    l=[]
    for i in range(30):
        p=randint(0,20)
        l.append(p)
    return l

"""A2 Écrire une fonction lancer_des()qui crée une liste de trois entiers tirés au sort entre 1 et 6, l’affiche, puis affiche “BRAVO” si un 6 figure dans la liste. - pas de return"""

def lancer_des():
    l=[]
    for i in range(3):
        o=randint(1, 6)
        l.append(o)
    for item in range (len(l)):
        if l[item]==6:
            print("BRAVO")

"""A3 Écrire une fonction mod_liste()qui crée une liste L d’au moins 5 entiers puis successivement : (pas de return)
l’affiche toute entière
affiche la valeur de L[4]
modifie la liste en remplaçant L[1]  par 17 et L[3] par la somme des cases voisines L[2] et L[4] puis l’affiche.
affiche 12 fois la valeur du dernier terme de la liste    """

def mod_liste():
    L=[]
    for i in range (randint(5,50)):
        o= randint(1, 100)
        L.append(o)
    print("la liste est :" ,L)
    print("le 5eme terme de la liste est : " ,L[4])
    L[1]=17
    print("le 2eme terme de la liste modifié est : ", L[1])
    L[3]=L[2]+L[4]
    print("Le 4eme terme de la liste modifié est : ",L[3])
    print("le dernier terme de la liste écris 12 fois : ", end="")
    for i in range(12):       
        print(L[-1],)
    
"""A4 Écrire une fonction change_bouts(L)qui échange les valeurs de la première et de la dernière case d’une liste quelconque non vide et la retourne"""

def change_bouts():
    l=[]
    for i in range (randint(1,50)):
        o= randint(1, 100)
        l.append(o)
    print(l)
    #print(l[0],l[-1])
    a=l[0]
    l[0]=l[-1]
    l[-1]=a
    return l[0],l[-1]

"""A5 Écrire une fonction enleve_tous(L,n) qui retire de la liste L toutes les occurrences de la valeur n et retourne la liste. Aide : pensez à la boucle while"""

def enleve_tous(l,n):  
    for ii in l:  
        while n in l:
            l.remove(ii)
    return l

"""B1 montre(L) qui affiche la liste L sur 2 colonnes (rang puis valeur) -pas de return-"""

def montre(l):
    for i in range(len(l)):
        print("Rang",i,"valeur",l[i])


"""B2  mult3(L) qui retourne le nombre de multiples de 3 présents dans la liste L"""

def mult3(l):
    a=0
    for i in l:
        if i%3==0:
            a=a+1 
    return a

"""B3  somm_paires(L) qui retourne la somme de toutes les valeurs paires de la liste L"""

def somm_paires(l):
    a=0
    for terme in l:
        if terme%2==0:
            a=a+terme
    return a

"""B4  extrem(L) qui retourne le minimum et le maximum des éléments de la liste L sous forme d’un tuple (sans recourir aux fonctions min() et max() toute faites)"""

def extrem(l):
    mi=l[0]
    ma=l[0]
    for item in range(len(l)):
        if mi>l[item]:
            mi=l[item]
        if ma<l[item]:
            ma=l[item]
    return ma,mi

"""B5  bravo(L) qui retourne le booléen True si la moyenne des valeurs de la liste L est supérieure ou égale à 15"""

def bravo(l):
    moy=0
    for terme in l:
        moy=moy+terme
    moy=moy/len(l)
    if moy >= 15:
        return True

""""B6  envers(L) qui affiche la liste L à l’envers (sans la modifier)  - pas de return -"""

"""PARTIE A
A1 - Ecrire une fonction supp_doublons(L) qui supprime les doublons d'une liste
     AIDE : Une idée d'algorithme est d'en écrire une nouvelle à partir de la liste donnée par une boucle de parcours."""
     
def supp_doublons(l):
    l2=[]
    for terme in l:
        if terme not in l2 :
            l2.append(terme)
    return l2


"""A2 - Ecrire une fonction mult_7_no_2_5(deb,fin) qui trouve tous les entiers compris entre deb et fin (les deux inclus) et qui sont multiples de 7 mais non multiples de 2 ni de 5. La fonction les retourne sous forme d'une liste"""

def mult_7_no_2_5(l,deb,fin):
    l2=[]
    for i in range(deb,fin):
        if l[i]%7==0 and l[i]%2>0 and l[i]%5>0:
            l2.append(l[i])
    return l2

"""A3 - Soit la liste  Animaux=[['girafe','Afrique',3000],['Loup','Europe',30],['Castor','Amérique',15],['Cheval','Europe',450]]  qui donne pour plusieurs animaux le nom, le continent principal, le poids moyen en kg.
Remarquez que c'est une liste de listes (parfois appelé tableau), vous pouvez facilement la compléter.
Ecrire une fonction qui admet cette liste comme paramètre et retourne la liste des noms (seulement les noms) d'animaux d'Europe de moins de 100kg (ou égal)"""

