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

racine = ArbreBinaire('25')#haut de l arbre
racine.insert_gauche('10') #la feuille a gauche de la racine
racine.insert_droit('60')  #la feuille a droite de la racine

dix_node = racine.get_gauche() #nouvel arbre avec comme haut de l arbre la feuille gauche de la racine originel
dix_node.insert_gauche('05')#la feuille a gauche de la 'nouvelle' racine
dix_node.insert_droit('20')#la feuille a droite de la 'nouvelle' racine

soixante_node = racine.get_droit() #nouvel arbre avec comme haut de l arbre la feuille droite de la racine originel
soixante_node.insert_gauche('35')#la feuille a gauche de la 'nouvelle' racine
soixante_node.insert_droit('65')#la feuille a droite de la 'nouvelle' racine

trente_cinq_node = soixante_node.get_gauche()#nouvel arbre avec comme haut de l arbre la feuille gauche d'une de la racine 'F'
trente_cinq_node.insert_gauche('30')#la feuille a droite de la 'nouvelle' racine
trente_cinq_node.insert_droit('45')

soixante_cinq_node = soixante_node.get_droit()#nouvel arbre avec comme haut de l arbre la feuille droite d'une de la racine 'F'
soixante_cinq_node.insert_droit('70')#la feuille a droite de la 'nouvelle' racine

quarante_cinq_node = trente_cinq_node.get_droit()
quarante_cinq_node.insert_gauche('40')
quarante_cinq_node.insert_droit('50')

cinquante_node = quarante_cinq_node.get_droit()
cinquante_node.insert_droit('55')

vingt_node = dix_node.get_droit()
vingt_node.insert_gauche('15')

dfezu=[25,60,35,10,5,20,45,64,45,70,40,50,55,30,15]

def parc_pref(t):
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
def parc_pref2(t):
    if t==None:
        return []
    else:
        return [t.get_valeur()] + parc_pref2(t.get_gauche())+ parc_pref2(t.get_droit())

def parc_suf(t):
    if t==None:
        return []
    else:
        return   parc_suf(t.get_gauche())+ parc_suf(t.get_droit())+[t.get_valeur()]
    
def parc_inf(t):
    if t==None:
        return []
    else:
        return   parc_inf(t.get_gauche())+[t.get_valeur()] +parc_inf(t.get_droit())
    
def sort_arbin(L):
    if not L:  # Si la liste est vide
        return []

    # Fonction pour insérer une valeur dans l'arbre
    def inserer_dans_arbre(arbre, valeur):
        if valeur < arbre.get_valeur():
            if arbre.get_gauche() is None:
                arbre.insert_gauche(valeur)
            else:
                inserer_dans_arbre(arbre.get_gauche(), valeur)
        else:
            if arbre.get_droit() is None:
                arbre.insert_droit(valeur)
            else:
                inserer_dans_arbre(arbre.get_droit(), valeur)
   
    # Création de l'arbre avec le premier élément
    arbre = ArbreBinaire(L[0])

    # Insertion des autres éléments dans l'arbre
    for valeur in L[1:]:
        inserer_dans_arbre(arbre, valeur)
    return parc_inf(arbre)

def est_dans(val,arb):
    return val in parc_suf(arb) 



