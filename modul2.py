def aktif ():
    global top
    a=int(input("kasa hesabi gir"))
    b=int(input("alınan cek hesabı gir"))
    c=int(input("bankalar hesabı"))
    d=int(input("alınacak senetler hesabı"))
    e=int(input("ticari mal hesabı"))
    f=int(input("binalar hesabi"))
    g=int(input("tasitlar hesabi"))
    h=int(input("demirbaslar hesabi"))
    top=a+b+c+d+e+f+g+h
    print(top)
    return top
def pasif ():
    global toplam
    a=int(input("banka kredileri"))
    b=int(input("saticılar hesabi"))
    c=int(input("banka kredileri hesabi"))
    d=int(input("borc senetleri hesabi"))
    e=int(input("sermaye hesabi"))
    toplam=a+b+c+d+e
    print(toplam)
    return toplam


