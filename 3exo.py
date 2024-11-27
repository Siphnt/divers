import csv

def exo1(l):
    animaux=[{'nom': 'girafe', 'poids': 1100, 'taille': 5.0}, {'nom': 'singe','poids': 70, 'taille': 1.75}] 
    leger=[l[0]['nom'],l[0]['poids']]
    lourd=[l[0]['nom'],l[0]['poids']]
    moy=0
    for p in l:
        if p['poids']<leger[1]:
            leger=p['nom'],p['poids']
        if p['poids']>lourd[1]:
            lourd=p['nom'], p['poids']
        moy=moy+p['poids']
    moy=moy/len(l)
        
    return 'L animale de plus leger est :' + leger[0] + ' avec un poids de '  + str(leger[1])+'kg','L animale de plus lourd est :' + lourd[0] + ' avec un poids de ' + str(lourd[1])+'kg','le poids moyen est de '+str(moy)+'kg'



def exo2():
    reader = csv.DictReader(open('titanic.csv', 'r'))
    tita = []
    rep=[]
    for row in reader:
        tita.append(dict(row))
    for cabin in tita:
        if cabin['Cabin'] != '':
            if cabin['Cabin'][0]=='C':
                rep.append(cabin)
    print(len(rep))   # impression des deux premières lignes
    
def exo3(t,n,var):
    a=0
    rep=[]
    for truc in range(len(t)):
        if truc==n:
            rep.append(var)
            rep.append(t[truc])
        else:
            rep.append(t[truc])
        
    return tuple(rep),t

def moy_age():
    reader = csv.DictReader(open('titanic.csv', 'r'))
    tita = []
    moyagevie=0
    vie=0
    moyagemort=0
    mort=0
    for row in reader:
        tita.append(dict(row))
    for cabin in tita:
        if cabin['Age'] != '':
            if cabin['Survived']=='1':
                moyagevie=moyagevie+float(cabin['Age'])
                vie=vie+1
            if cabin['Survived']=='0':
                moyagemort=moyagemort+float(cabin['Age'])
                mort=mort+1
    moyagemort=moyagemort/mort
    moyagevie=moyagevie/vie
    print(moyagevie,moyagemort)   # impression des deux premières lignes