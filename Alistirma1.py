# Teşekkür ederim Mete arkadaşım :) <3
import random
sinir = input("Oyunu kaç kez oynamak istediğinizi giriniz: ") # Kullanıcı oyunu kaç kez oynamak istediğini belirler
while sinir.isdigit() == False: # Kullanıcı sınırı sayıyla ifade etmek zorundadır.
    sinir = input("Lütfen bir sayıyla ifade ediniz: ")
sinir = int(sinir) # While döngüsünde kullanabilmemiz için int'e çevirmemiz gerekir.
sayac = 0
dogruyer = 0
yanlisyer = 0
while sayac < sinir:
    if sayac == 0: # Her seferinde şartları hatırlatmasına gerek yok diye düşündüğümden farklılık olsun diye diğer girdi inputları farklı bir cümleyle veriyi istiyor
        girdi = input("Lütfen iki basamaklı ve her iki basamağı da farklı rakamlardan oluşan bir sayı seçiniz: ")
    else:
        girdi = input("\nŞimdi tekrar bir sayı giriniz: ")
    if girdi.isdigit() == True and len(girdi) == 2 and girdi[0] != 0 : # Girdinin istenen tüm özellikleri bunlar
        sayi = str(random.randint(10,98))
        while sayi[0] == sayi[1]: # Basamakların aynı olması durumu
            sayi = str(random.randint(10,98))
        print("Programın seçtiği sayı: ",sayi) # Programın doğru çalışıp çalışmadığını kontrol etmek için var
        if girdi[0] == sayi[0] or girdi[-1] == sayi[-1]:
            dogruyer += 1
        elif girdi[0] == sayi[-1] or girdi[-1] == sayi[0]:
            yanlisyer += -1
        sayac += 1 # Kullanıcı sayıyı yanlış girdiğinde sayaç devreye girmez yani sınırın sayacı ancak doğru veriyle çalışır.
    else:
        girdi = input("Lütfen belirtilen şartlara uygun bir sayı giriniz: ")
print("\nDoğruyer sayacının değeri: ",dogruyer)
print("Yanlışyer sayacının değeri: ",yanlisyer)
