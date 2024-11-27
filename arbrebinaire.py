####### début de la classe contenant diverses fonctions ########
####### nécessaires à la constructions d'arbres binaires ########

class ArbreBinaire:		# UN ARBRE POSSEDE DEUX ENFANTS (noeuds D et G) EUX-MEMES DES ARBRES
    def __init__(self, valeur):
        self.valeur = valeur		# affecte une valeur au noeud
        self.enfant_gauche = None		# prévoit les attributs enfants G et D
        self.enfant_droit = None		# sans affecter de valeur (none)

    def insert_gauche(self, valeur):	# INSERTION N'IMPORTE OU AVEC DECALAGE SI PLACE OCCUPEE
        if self.enfant_gauche == None:			# si place libre
            self.enfant_gauche = ArbreBinaire(valeur)	# instanciation nouvel arbre et accrochage
        else:					# si place pas libre (occupée par arbre x)
            new_node = ArbreBinaire(valeur)		# création d'un nouvel arbre avec nouvelle valeur
            new_node.enfant_gauche = self.enfant_gauche	# accrochage de l'abre x à gauche du nouveau
            self.enfant_gauche = new_node			# accrochage du nouveau à la place initialement occupée

    def insert_droit(self, valeur):
        if self.enfant_droit == None:
            self.enfant_droit = ArbreBinaire(valeur)
        else:
            new_node = ArbreBinaire(valeur)
            new_node.enfant_droit = self.enfant_droit
            self.enfant_droit = new_node

    def get_valeur(self):
        return self.valeur

    def get_gauche(self):
        return self.enfant_gauche

    def get_droit(self):
        return self.enfant_droit
      

    def __repr__(self):
        if self != None:
            return '('+self.get_valeur()+','+self.get_gauche().__repr__()+','+self.get_droit().__repr__()+')'
    
###########  fin de la classe (les fonctions outils)  ########
      
  
## début de la construction de l'arbre binaire donné en exemple ##

racine = ArbreBinaire('A')#haut de l arbre
racine.insert_gauche('B') #la feuille a gauche de la racine
racine.insert_droit('F')  #la feuille a droite de la racine

b_node = racine.get_gauche() #nouvel arbre avec comme haut de l arbre la feuille gauche de la racine originel
b_node.insert_gauche('C')#la feuille a gauche de la 'nouvelle' racine
b_node.insert_droit('D')#la feuille a droite de la 'nouvelle' racine

f_node = racine.get_droit() #nouvel arbre avec comme haut de l arbre la feuille droite de la racine originel
f_node.insert_gauche('G')#la feuille a gauche de la 'nouvelle' racine
f_node.insert_droit('H')#la feuille a droite de la 'nouvelle' racine

c_node = b_node.get_gauche()#nouvel arbre avec comme haut de l arbre la feuille gauche d'une de la racine 'B'
c_node.insert_droit('E')#la feuille a droite de la 'nouvelle' racine

g_node = f_node.get_gauche()#nouvel arbre avec comme haut de l arbre la feuille gauche d'une de la racine 'F'
g_node.insert_gauche('I')#la feuille a droite de la 'nouvelle' racine

h_node = f_node.get_droit()#nouvel arbre avec comme haut de l arbre la feuille droite d'une de la racine 'F'
h_node.insert_droit('J')#la feuille a droite de la 'nouvelle' racine

######  fin de la construction de l'arbre binaire  ###########
"""
racine = ArbreBinaire('S')
racine.insert_gauche('A')
racine.insert_droit('H')

a_node = racine.get_gauche()
a_node.insert_gauche('O')
a_node.insert_droit('U')

h_node = racine.get_droit()
h_node.insert_gauche('T')
h_node.insert_droit('J')

o_node =a_node.get_gauche()
o_node.insert_gauche('R')

t_node = h_node.get_gauche()
t_node.insert_droit('M')

j_node = h_node.get_droit()
j_node.insert_droit('K')"""
"""
racine = ArbreBinaire('A')#haut de l arbre
racine.insert_gauche('B') #la feuille a gauche de la racine
racine.insert_droit('F')  #la feuille a droite de la racine

b_node = racine.get_gauche() #nouvel arbre avec comme haut de l arbre la feuille gauche de la racine originel
b_node.insert_gauche('C')#la feuille a gauche de la 'nouvelle' racine
b_node.insert_droit('D')#la feuille a droite de la 'nouvelle' racine

f_node = racine.get_droit() #nouvel arbre avec comme haut de l arbre la feuille droite de la racine originel
f_node.insert_gauche('G')#la feuille a gauche de la 'nouvelle' racine
f_node.insert_droit('H')#la feuille a droite de la 'nouvelle' racine


g_node = f_node.get_gauche()#nouvel arbre avec comme haut de l arbre la feuille gauche d'une de la racine 'F'
g_node.insert_gauche('I')#la feuille a droite de la 'nouvelle' racine
g_node.insert_droit('X')

h_node = f_node.get_droit()#nouvel arbre avec comme haut de l arbre la feuille droite d'une de la racine 'F'
h_node.insert_droit('J')#la feuille a droite de la 'nouvelle' racine
h_node.insert_gauche('Y')"""
def taill(t):
    if not t:
        return 0
    return taill(t.get_droit())+taill(t.get_gauche())+1

def hauteur(t):
    if not t:
        return -1
    return max(hauteur(t.get_droit()),hauteur(t.get_gauche()))+1

def parvour_large(t):
    rep=[]
    file=[t]
    while file :
        arb=file.pop(0)
        rep.append(arb.get_valeur())
        if arb.get_gauche():
            file.append(arb.get_gauche())
        if arb.get_droit():
            file.append(arb.get_droit())
    return rep
def parvour_prof(t):
    rep=[]
    file=[t]
    while file :
        arb=file.pop(-1)
        rep.append(arb.get_valeur())
        if arb.get_gauche():
            file.append(arb.get_gauche())
        if arb.get_droit():
            file.append(arb.get_droit())
    return rep   

def parvour_prof2(t):
    rep=[]
    file=[t]
    while file :
        arb=file.pop(-1)
        rep.append(arb.get_valeur())
        if arb.get_droit():
            file.append(arb.get_droit())
        if arb.get_gauche():
            file.append(arb.get_gauche())
        
    return rep   
def loc_compl(t):
    # Si l'arbre est vide, il est considéré comme complet
    if t is None:
        return True
    # Vérifie si les enfants gauche et droit sont tous les deux présents
    if type(t.get_gauche()) != type(t.get_droit()):
        return False

    # Récursion pour vérifier les sous-arbres
    return loc_compl(t.get_gauche()) and loc_compl(t.get_droit())
