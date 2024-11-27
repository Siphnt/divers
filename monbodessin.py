#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 09:37:21 2023

@author: jp.giard
"""
#######################################################
# Import du module turtle                             #
#               (une sorte de complément à Spyder)    #
#######################################################
import turtle

#######################################################
#              préparation de la fenêtre              #
#######################################################
turtle.setup(640, 480, 100, 100)  #Largeur : 640px, Hauteur : 480px, pos x : 100px, pos y : 100px
turtle.title("Ma super fenêtre")  #Change le titre


#######################################################
#            préparation du (des) crayon(s)           #
#######################################################
crayon=turtle.Turtle()


#######################################################
#            Instructions de dessin                   #
#######################################################
import random
couleurs=['pink','green','red','yellow','blue','purple']
turtle.speed(0)
def rond(x,y) :
    for i in range (30) :
        crayon.forward(x)
        crayon.right(100)

for taille in range(10,500,5):
    x=random.randint(-320,320)
    y=random.randint(-240,240)
    crayon.up()
    crayon.goto(x,y)
    crayon.down()
    couleur=random.choice(couleurs)
    crayon.color(couleur)
    rond(taille,6)