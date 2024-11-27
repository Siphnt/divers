def maj(texte):
    maj=' '
    for lettre in texte :      
        lettre=ord(lettre) #on transforme les lettre en chiffre
        if 97<=lettre<=122: #pour etre que dans des miniscules
            lettre=lettre-32 #on enlève 32 pour mettre en majuscule
            lettre=chr(lettre) #on remet les chifres en lettre
            maj=maj+lettre
        else :
            lettre=chr(lettre)
            maj=maj+lettre
    return maj 

def cesar(text,n):
    mot=''
    for lettre in text:
        lettre=ord(lettre)
        if 97<=lettre<=122 :
            lettre=lettre+n
            if lettre>122:
                lettre=lettre-26
            elif lettre<97 :
                lettre=lettre+26
            lettre=chr(lettre)
            mot=mot+lettre
        else :
            lettre=chr(lettre)
            mot=mot+lettre            
    return mot

def cesar1(text,n):
    mot=''
    for lettre in text:
        lettre=ord(lettre)
        if 97<=lettre<=122 :
            lettre=lettre-n
            if lettre>122:
                lettre=lettre-26
            elif lettre<97 :
                lettre=lettre+26
            lettre=chr(lettre)
            mot=mot+lettre
        else :
            lettre=chr(lettre)
            mot=mot+lettre            
    return mot

def vigen(cle, text):
    l1=len(text)
    l2=len(cle)
    mult=l1//l2+1
    cl=mult*cle
    #print(cl)
    mot=''
    for ltxt, lcle in zip(text, cl):
        #print(ltxt, 'se code avec', lcle)
        lcle=ord(lcle)
        lcle=lcle-97
        test= cesar(ltxt, lcle)
        mot=mot+test
    return mot

def vigen1(cle, text):
    l1=len(text)
    l2=len(cle)
    mult=l1//l2+1
    cl=mult*cle
    #print(cl)
    mot=''
    for ltxt, lcle in zip(text, cl):
        #print(ltxt, 'se code avec', lcle)
        lcle=ord(lcle)
        lcle=lcle-97
        test= cesar1(ltxt, lcle)
        mot=mot+test
    return mot