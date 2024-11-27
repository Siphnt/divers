def code_shad(n):
    if n==0 :
        return'0'
    mot=''
    while n>=1:
        signe=n%4
        if signe ==0:
            signe='Ga'
        if signe ==1:
            signe='Bu'
        if signe ==2:
             signe='Zo' 
        if signe ==3:
            signe='Meu'
        n=n//4
        mot=signe+mot
         
    return mot

def bin_to_dec(mot):
    val=8
    total=0
    for signe in mot :
        total=total+int(signe)*val
        val=val//2
    return total

def bin_to_hex(mot):
    p1=mot [:4]
    p2=mot [4:]
    z1=bin_to_dec(p1)
    z2=bin_to_dec(p2)
    if z1>10:
        if z1==10 :
            print("A")
        elif z1==11 :
            print("B")
        elif z1==12 :
            print("C")
        elif z1==13 :
            print("D")
        elif z1==14 :
            print("E")
        elif z1==15 :
            print("F")
    elif z1<10:
        print(z1)
    elif z2>10:
        if z2==10 :
            print("A")
        elif z2==11 :
            print("B")
        elif z2==12 :
            print("C")
        elif z2==13 :
            print("D")
        elif z2==14 :
            print("E")
        elif z2==15 :
            print("F")
    elif z2<10:
        print(z2)
    