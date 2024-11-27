class Rectangle:
    def __init__(self,longueur,largeur):
        self.longueur=longueur
        self.largeur=largeur

        
    def __repr__(self):
        return "Rectangle de lageur " + str(self.largeur)+" et de longueur "+str(self.longueur)
    
    def allonge(self,delta):
        
        if delta<=-self.longueur:
            return 'No.'
        else :
            self.longueur+=delta
            if self.longueur<self.largeur:
                self.longueur,self.largeur=self.largeur,self.longueur
    def surface(self):
        return self.longueur*self.largeur
    def peri(self):
        return self.longueur*2+self.largeur*2
        

class Fraction:
    def __init__(self,numerateur,denominateur):
        if denominateur == 0:
            raise BaseException("dénominateur ne peut pas être nul")
        self.numerateur=numerateur
        self.denimonateur=denominateur
        
        
    def __repr__(self):
        return str(self.numerateur)+"\n"+"---"+"\n"+str(self.denimonateur)
    
    def calcule(self):
        return self.numerateur/self.denimonateur
    
    def mult(self, frac2):
        self.numresult=self.numerateur*frac2.numerateur
        self.denumresult=self.denimonateur*frac2.denimonateur
        return Fraction(self.numresult,self.denumresult)
        
    def augmente(self,frac2):
        if  self.denimonateur != frac2.denimonateur:
            frac2.numerateur=frac2.numerateur*self.denimonateur
            self.numerateur=self.numerateur*frac2.denimonateur
            self.denimonateur= self.denimonateur*frac2.denimonateur
        self.numerateur=self.numerateur+frac2.numerateur
        for a in range(self.denimonateur,1,-1):
            if self.denimonateur%a == 0 and self.numerateur%a==0:
                print(self.numerateur)
                self.denimonateur=int(self.denimonateur/a)
                self.numerateur=int(self.numerateur/a)
                print(self.numerateur,a)
                
                
                
                
                
