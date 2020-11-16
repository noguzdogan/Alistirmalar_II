import random
sinir = input("Oyunu kaç kez oynamak istediğinizi giriniz: ")
while sinir.isdigit() == False:
    sinir = input("Lütfen bir sayıyla ifade ediniz: ")
sinir = int(sinir)
sayac = 0
dogruyer = 0
yanlisyer = 0
while sayac < sinir:
    if sayac == 0:
        girdi = input("Lütfen iki basamaklı ve her iki basamağı da farklı rakamlardan oluşan bir sayı seçiniz: ")
    else:
        girdi = input("\nŞimdi tekrar bir sayı giriniz: ")
    if girdi.isdigit() == True and len(girdi) == 2 and girdi[0] != 0 and girdi[0] != girdi[1]: # Girdinin istenen tüm özellikleri bunlar
        sayi = str(random.randint(10,98))
        while sayi[0] == sayi[1]:
            sayi = str(random.randint(10,98))
        print("Programın seçtiği sayı: ",sayi)
        if girdi[0] == sayi[0]:
            dogruyer += 1
        elif girdi[-1] == sayi[-1]:
            dogruyer += 1
        elif girdi[0] == sayi[-1]:
            yanlisyer += -1
        elif girdi[-1] == sayi[0]:
            yanlisyer += -1
        sayac += 1
    else:
        girdi = input("Lütfen belirtilen şartlara uygun bir sayı giriniz: ")
print("\nDoğruyer sayacının değeri: ",dogruyer)
print("Yanlışyer sayacının değeri: ",yanlisyer)



