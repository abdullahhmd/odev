def katmadegerciro (x,y,z,q,w):
    global KdegerCiro
    KdegerCiro=x-(y+z+q+w)
    if KdegerCiro > 1000 :
        print("isletme katma deger cirosu yuksek")
    elif 500 < KdegerCiro < 999 :
        print("isletme katma deger cirosu normal")
    else:
        print("isletme katma deger cirosu dusuk") 
x=int(input("toplam satıs mik gir"))
y=int(input("hammadde maliyeti gir"))
z=int(input("bakım onarım gideri gir"))
q=int(input("sevkiyat giderleri gir"))
w=int(input("satın alınan hizmet giderleri gir"))
katmadegerciro(x,y,z,q,w)
