toplam=0
while True:
    print("Bir sayi giriniz,Cıkıs icin 0(sıfır)")
    girilen=int(input("sayi: "))
    if(girilen!=0):
        a=girilen%3
        toplam=toplam+a
        print("toplam=",toplam)
    else:
        print("cıkıs yapıldı")
        break
