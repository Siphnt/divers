def jeulusmoin():
    import random 
    nombre=random.randint(0,1000) #tiré au hasard le nombre cible   
    a=1
    i=0#nombre d essaie
    while a==1 : #boucle infnie
        guess=int(input("donne un nombre"))#demande un nombre
        i=i+1#augmente le nombre d essaie a chaque erreur
        if nombre-5<guess<nombre+5:
            a=2#sort de la boucle infinie
        elif guess>nombre : #si moins que le nombre écris "moins"
            print("moins")
        elif guess<nombre :#si plus que le nombre écris "plus"
            print("plus")
    print("gg vous avez trouvé en",i,"essaie")#écris le nombre d essaie fait