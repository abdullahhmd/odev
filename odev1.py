print ("kar etmismi etmemismi")
finansman_gelir=int(input("finansman gelir yazınız"))
pazar_gelir=int(input("pazar gelir yazın"))
kira_gelir=int(input("kira gelir yazın"))
ucret=int(input("ucret girin"))
finansman_gider=int(input("finansman gider yazın"))
pazar_gider=int(input("pazar gider yazın"))
kira_gider=int(input("kira gider yazın"))
muhasebe_gider=int(input("muhasebe gider"))
gelir=(finansman_gelir+pazar_gelir+kira_gelir)
gider=ucret+finansman_gider+pazar_gider+kira_gider+muhasebe_gider
kar=gelir-gider
if kar> 1000 :
    print ("karli")
elif kar == 1000 :
    print ("basabas")
else:
    print ("zarar ettiniz")
