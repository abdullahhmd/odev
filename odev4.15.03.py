x=int(input("koltuk girin"))
y=int(input("yatak girin"))
z=int(input("dolap girin"))
def donembasıstok ():
    global ilkstok
    ilkstok=x+y+z
    return ilkstok
def donemsonustok():
    global sonstok
    w=x+35
    e=y+35
    r=z+15
    sonstok=w+e+r
    return sonstok
a=donembasıstok()
b=donemsonustok()

ortalamastok=(a+b)/2
print("ortalama stok hesaplama=",ortalamastok)
