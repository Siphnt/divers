class File:
    def __init__(self):
        self.file=[]
        
        
    def __repr__(self):
        return 'tete <-'+str(self.file)+'<-queue'
    
    def enfile(self,donne):
        if len(self.file)<1024:
            self.file.append(donne)
        else:
            return "Pile full"
    def defile(self):
        self.truc=self.file[0]
        del self.file[0]
        return self.truc
    
    def est_vide(self):
        return len(self.file)==0
    
    def sommet(self):
        self.defile()
        self.enfile(self.truc)
        return self.truc
    
    def file_pleine(self):
        return len(self.file)==1024
    
    def tete(self):
        svg=File()
        rep=self.defile()
        svg.enfile(rep)
        while not self.est_vide():
            svg.enfile(self.defile())
        self.file=svg.file
        return rep
    
    def tourne(self,n):
        for _ in range(n):
            self.enfile(self.defile())
            
def trie(file):
    paire=File()
    impaire=File()
    while not file.est_vide():
        a=file.defile()
        if a%2==0:
            paire.enfile(a)
        else :
            impaire.enfile(a)
    return paire,impaire

def route(route1,roue2):
    route3=File()
    