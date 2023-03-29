isim = str(input("isim : "))
yas = int(input("yaş : "))
egitim = str(input("eğitim durumu : "))

if (yas >= 18):
    if (egitim == "üniversite" or egitim == "lise"):
        print("ehliyet alabilirsiniz")
    else:
        print("ehliyet alamazsınız, eğitim durumu yetersiz")
else:
    print("ehliyet alamazsınız, yaş yetersiz")

##########################################################

import datetime

tarih = input('aracınız hangi tarihte trafiğe çıktı (yıl/ay/gün): ')
tarih = tarih.split('/')

trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi = datetime.datetime.now()

days = simdi - trafigeCikis
print(days)
