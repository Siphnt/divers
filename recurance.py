def conv(rome):
    rom={'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1} 
    if len(rome)==1:
        return rom[rome]
    else:
        if rom[rome[0]]<rom[rome[1]]:
            return -rom[rome[0]] + conv(rome[1:])
        else :
            return rom[rome[0]] + conv(rome[1:])
        
        