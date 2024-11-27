#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 08:29:20 2021

@author: jp.giard
"""

#################################################################################################################
#  Récupoérer sous forme de liste de dictionnaires le tableau csv des textes de référence en langues connues    #
#                                                                                                               #
#  Informations ainsi exploitables dans le programme python pour calculer la "distance" du texte inconnu avec   # 
#  chacun des textes de référence                                                                               #
#################################################################################################################


import csv
reader = csv.DictReader(open('lettres_langues.csv', 'r'))
ref_lang = []
for row in reader:
    ref_lang.append(dict(row))
    
    
# exemple d'utilisation ci-dessous
#      accéder aux taux de H du 5ème texte de reference
#print(ref_lang[4]['taux_H'])
def quelle_langue(texte):
    texte=texte.upper()
    mon_h=0
    mon_u=0
    long=len(texte)
    ref_lang = []
    lang=[]
    a=()
    reader = csv.DictReader(open('lettres_langues.csv', 'r'))
    ref_lang = []
    for row in reader:
        ref_lang.append(dict(row))
    for row in reader:
       ref_lang.append(dict(row))
    for lettre in texte:
        if lettre == 'U':
            mon_u=mon_u+1
        elif lettre == 'H':
            mon_h=mon_h+1
        elif lettre == ' ':
            long=long-1
        elif lettre == ',':
           long=long-1         
    mon_h=(mon_h/long)*100
    mon_u=(mon_u/long)*100
    for i in range(len(ref_lang)):
        a=(((((float(ref_lang[i]['taux_H'])-mon_h)**2+(float(ref_lang[i]['taux_U'])-mon_u)**2)**0.5)),(ref_lang[i]['langue']),)
        lang.append(a)
    lang.sort()
    print(lang[0][1],lang[1][1],lang[2][1],lang[3][1],)

def apprendre(texte,l):
    ref_lettre=['O','T','N','A','H','P']
    ref_langue={}
    b=()
    mon_o=0
    mon_t=0
    mon_n=0
    mon_a=0
    mon_h=0
    mon_p=0
    long=len(texte)
    for lettre in texte:
        if lettre=='o':
            mon_o=mon_o+1
        elif lettre=='t':
            mon_t=mon_t+1
        elif lettre=='n':
            mon_n=mon_n+1
        elif lettre=='a':
            mon_a=mon_a+1
        elif lettre=='h':
            mon_h=mon_h+1
        elif lettre=='p':
            mon_p=mon_p+1
        elif lettre==' ' or '.' or ';' or ':' or '?' or '!' or '/':
            long=long-1
    mon_o=(mon_o/long)*100
    mon_t=(mon_t/long)*100
    mon_n=(mon_n/long)*100
    mon_a=(mon_a/long)*100
    mon_h=(mon_h/long)*100
    mon_p=(mon_p/long)*100
    #b=[(mon_o),(mon_t), (mon_n), (mon_a), (mon_h), (mon_p),(l),]
    ref_langue[(l)]=[(mon_o),(mon_t), (mon_n), (mon_a), (mon_h), (mon_p),]
    print(ref_langue)