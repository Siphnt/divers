class Pile:
    def __init__(self):
        self.pile=[]
        
        
    def __repr__(self):
        return str(self.pile)
    
    def empile(self,donne):
        if len(self.pile)<1024:
            self.pile.append(donne)
        else:
            return "Pile full"
    def depile(self):
        self.truc=self.pile[-1]
        del self.pile[-1]
        return self.truc
    
    def est_vide(self):
        if len(self.pile)>0:
            return False
        else: 
            return True
    
    def sommet(self):
        self.depile()
        self.empile(self.truc)
        return self.truc
    
    def pile_pleine(self):
        return len(self.pile)==1024
    

        
        

def empile(pile,donne):
    pile.append(donne)
    
def depile(pile):
    if len(pile)>0:
        depile1=pile[-1]
        del pile[-1]
        return int(depile1)
def inverse(pile):
    pile2=[]
    for i in range(len(pile)-1,0,-1):
        pile2.append(pile[i])
    pile2.append(0)
    return pile2

def prof_max(pile):
    pile2=[]
    maxi=pile[-1]
    for i in range(len(pile)):
        pile2.append(depile(pile))
        if len(pile)>0:
            if maxi<pile2[i]:
                maxi=pile2[i]
    for a in range(len(pile2)-1,0,-1):
        empile(pile,pile2[a])
    empile(pile,pile2[0])
    return maxi,pile
        