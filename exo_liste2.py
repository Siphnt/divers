def nb_repetitions(elt,tab):
    rep=0
    for valeur in tab :
        if valeur == elt:
            rep=rep+1
    return rep

def moyenne(liste):
    moy=0
    for valeur in liste:
        moy=moy+valeur
    if len(liste)==0:
        return 'Erreur'
    moy=moy/len(liste)
    return moy

def recherche(elt,tab):
    rep=-1
    for indice in range(len(tab)):
        if elt==tab[indice]:
            rep=indice
    return rep

def recherche1(lettre,mot):
    rep=0
    for truc in mot:
        if truc == lettre:
            rep=rep+1
    return rep

def renverse(mot):
    rep=''
    for lettre in mot :
        rep=lettre+rep
    return rep

def min_et_max(tab):
    rep={'mini':tab[0],'maxi':tab[0]}
    
    for valeur in tab:
        if valeur >rep['maxi']:
            rep['maxi']=valeur
        if valeur < rep['mini']:
            rep['mini']=valeur
    return rep

def enumere(L):
    rep={}
    recherche=[] 
    a=0
    for _ in range(len(L)-1):
        for indice in range(len(L)):
            if L[indice]==L[a]:
                recherche.append(indice)
        rep[L[a]]=recherche
        a=a+1
        recherche=[]          
    return rep

def compte(mot):
    rep={}
    a=0
    b=0
    for _ in range(len(mot)-1):
        for indice in range(len(mot)):
            if mot[a]==mot[indice]:
                b=b+1
        rep[mot[a]]=b
        a=a+1
        b=0
    return rep