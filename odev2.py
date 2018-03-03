def oee ():
    pus=int(input("planlanmis uretim suresi gir"))
    psızd=int(input("plansız durus gır"))
    pus=int(input("planlanmıs uretim suresi"))
    scz=int(input("standart cevrim zamanı"))
    um=int(input("uretim miktari"))
    süm=int(input("saglam urun miktari"))
    tum=int(input("toplam uretim miktari"))
    kullanılabilirlik=(pus-psızd)/pus
    performans=(scz*um)/(pus-psızd)
    kalite=süm/tum
    ooe=kullanılabilirlik*performans*kalite
    return ooe
