calisan=50
yevmiye=90
aylik_mesai=0
haftalik_maas=90*7
aylik_maas=0
while aylik_mesai<=22:
    haftalik_mesai=int(input("haftalik mesai:"))
    aylik_mesai=haftalik_mesai*4
    haftalik_maas=haftalik_maas+(haftalik_mesai*yevmiye*0.10)
    aylik_maas=aylik_maas+haftalik_maas*4
    print("Aylik maas:",aylik_maas)
else:
    print("Aylik mesai 22 saaten fazla olamaz")
