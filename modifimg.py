from PIL import Image
import random
mon_im=Image.open('gojo.png')

largeur = mon_im.size[0]
hauteur = mon_im.size[1]
x=0
y=0
for i in range(hauteur):
    for a in range(largeur):
        (r,v,b)= mon_im.getpixel((a,i))
        moy=(r+v+b)/3
        moy=int(moy)
        mon_im.putpixel((a,i),(moy,moy,moy))

hauteur2=int(hauteur/10)
largeur2=(int(largeur/10),int(largeur/10)*2,int(largeur/10)*3,int(largeur/10)*4,int(largeur/10)*5,int(largeur/10)*6,int(largeur/10)*7,int(largeur/10)*8,int(largeur/10)*9,int(largeur/10)*10)
print(hauteur2)
"""for i in range(10):
    for a in range(largeur):
        mon_im.putpixel((a,y),(0,0,0))
    y=y+hauteur2

for i in range(hauteur):
    for a in range(10):
        mon_im.putpixel((largeur2[a],i),(0,0,0))"""


for i in range(hauteur):
    for a in range(largeur):
        (r,v,b)= mon_im.getpixel((a,i))
        #r,v,b=b,r,v
        #if 150<r<255:
            #r=0
        if 0<b<150:
            b=170
        b=random.randint(0,255)
        mon_im.putpixel((a,i),(r,v,b))
      
mon_im.show()