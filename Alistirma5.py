def super_asal(x):
    bolen = 0
    if x % 2 == 1 and x > 9: # 2 hariç tüm asal sayılar tek sayı olduğundan bu şart var
        max_bolen = int((x+1)/2) # Bu float tanımlanacağı için for döngüsüne uygun hale getirdim
        for y in range(2,max_bolen): # x'in yarısından fazlasının bölen olup olmadığını kontrol etmeye gerek yok.
            if x % y == 0: # Sayının asal olmama durumunu kontrol eder
                bolen += 1 # Bir sayı eğer süper asalsa 'bolen' değişkeni her zaman sıfıra denk olmalı
        if bolen == 0: # Böleni yoksa...
            temp = str(x) # Geçici bir string değeriyle çıkartma yapıcam
            temp_list = list(temp) # Bu da eleman atabilmek için kullanacağım liste değişkeni
            temp_list.pop() # Son elemanı şutluyorum
            temp = "" # Sıradaki işlem için temp değerinin içini boşaltıyorum.
            for z in range(0,len(temp_list)): # Her indisi tek tek temp'e tekrar ekliyorum. Ancak şimdi son eleman yok.
                temp += temp_list[z]
            x = int(temp) # Geçici değerimdeki yeni veriyi tekrar int'e çeviriyorum.
            return super_asal(x)
        else:
            return False
    elif (x in [2,3,5,7]) == True:
        return True
    else:
        return False
print("5 basamaklı süper asal sayılar:\n")
for n in range(1000,10000):
    n1 = n # İlk değeri saklıyorum
    if super_asal(n) == True:
        print(n1,end=" ")
