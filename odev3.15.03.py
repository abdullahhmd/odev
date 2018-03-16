def ilkaltiaygelir (x,y,z):
    global ilkgelir
    ilkgelir=x+y+z
    return ilkgelir
x=int(input("yazılım geliri gir"))
y=int(input("finansman geliri gir"))
z=int(input("ürün satıs geliri gir"))
def ilkaltiaygider (x,y,z):
    global ilkgider
    ilkgider=x+y+z
    return ilkgider
x=int(input("calısan maaslari"))
y=int(input("kira gider"))
z=int(input("donanım maliyet"))
def sonaltiaygelir (x,y,z,q):
    global songelir
    songelir=x+y+z+q
    return songelir
x=int(input("yazlım gelir gir"))
y=int(input("sponsorluk geliri"))
z=int(input("e ticaret geliri"))
q=int(input("ürün satıs geliri"))
def sonaltiaygider (x,y,z):
    global songider
    songider=x+y+z
    return songider
x=int(input("calısan maas"))
y=int(input("kira gider"))
z=int(input("bakım maliyeti"))
def isletmekari(x,y):
    kar=x-y
    if (kar>5000):
        print("isletme cok karlı")
    elif (1000<kar<5000):
        print("isletme karı normal")
    else:
        print("isletme yeterince karda degil")
gelirler=ilkaltiaygelir(x,y,z)+sonaltiaygelir(x,y,z,q)
giderler=ilkaltiaygider(x,y,z)+sonaltiaygider(z,y,z)
isletmekari(gelirler,giderler)
        
