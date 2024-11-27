#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 16:56:09 2023

@author: m.cossard22
"""

from random import*
import time



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



l3=[]
for i in range(50000):
    p=randint(0,100)
    l3.append(p)

TOPdebut=time.time()

toto=tri_sel(l3)

TOPfin=time.time()

duree=TOPfin-TOPdebut



print ('durée pour effectuer le programme',duree)

