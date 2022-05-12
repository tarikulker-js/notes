import os
import time
import math

"""

#Fonksiyona parametre gönderme

def merhabaFonksiyonlar(name, birthYear): 
    print("merhaba " + name + " yaşınız: " + str(2022 - birthYear))

merhabaFonksiyonlar("mal efekan", 2007)
"""
"""
#Fonksiyondan veri çekme

def getAge(birthYear):
    return 2022 - birthYear

print("Merhaba, yaşınız: " + str(getAge(2007)))
"""

"""
dogumYili = int(input("Dogum yılınızı bağışlar mısınız aslanım: "))

def yasHesapla(dogumYili):
    return 2022 - dogumYili

def emekliligeKalanYıl(dogumYili): 
    yas = yasHesapla(dogumYili)
    kalanYil = 65 - yas
    if kalanYil > 0:
        print("Emekliliğinize " + str(kalanYil) + " yıl kaldı")
    else:
        print("Zaten emeklisin yavrum")

emekliligeKalanYıl(dogumYili)

"""

islemNo = int(input(""" 

1) Toplama
2) Çıkarma
3) Çarpma
4) Bölme
5) Modunu alma
6) Karesini alma
7) Karekök
8) Tam bölme

Lütfen işlem numarası giriniz: """))

if islemNo > 8:
    print("Yanlış işlem numarası")
    print("Sistem yeniden başlatılıyor...")
    time.sleep(3)
    os.system("cls")
    os.system("python ./for.py")

if (islemNo == 6 or islemNo == 7):
    ilkSayi = int(input("Sayı: "))
else:
    ilkSayi = int(input("İlk sayı: "))
    ikinciSayi = int(input("İkinci sayı: "))

def topla(ilkSayi, ikinciSayi):
    return ilkSayi + ikinciSayi

def cikar(ilkSayi, ikinciSayi):
    return ilkSayi - ikinciSayi

def carp(ilkSayi, ikinciSayi):
    return ilkSayi * ikinciSayi

def bol(ilkSayi, ikinciSayi):
    return ilkSayi / ikinciSayi

def modunuAl(ilkSayi, ikinciSayi):
    return ilkSayi % ikinciSayi

def karesiniAl(ilkSayi):
    return ilkSayi * ilkSayi

def karekok(ilkSayi):
    return math.sqrt(ilkSayi)

def tamBol(ilkSayi, ikinciSayi):
    return ilkSayi // ikinciSayi

if islemNo == 1:
    print("Sonuç: " + str(topla(ilkSayi, ikinciSayi)))
elif islemNo == 2:
    print("Sonuç: " + str(cikar(ilkSayi, ikinciSayi)))
elif islemNo == 3:
    print("Sonuç: " + str(carp(ilkSayi, ikinciSayi)))
elif islemNo == 4:
    print("Sonuç: " + str(bol(ilkSayi, ikinciSayi)))
elif islemNo == 5:
    print("Sonuç: " + str(modunuAl(ilkSayi, ikinciSayi)))
elif islemNo == 6:
    print("Sonuç: " + str(karesiniAl(ilkSayi)))
elif islemNo == 7:
    print("Sonuç: " + str(karekok(ilkSayi)))
elif islemNo == 8:
    print("Sonuç: " + str(tamBol(ilkSayi, ikinciSayi)))
else:
    print("Yanlış işlem numarası")
    print("Sistem yeniden başlatılıyor...")
    time.sleep(3)
    os.system("cls")
    os.system("python ./for.py")