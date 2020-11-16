def fibonacci(x):
    if x == 1 or x == 2:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2) # bir önceki ve iki önceki fonksiyon değerini toplayıp yeni fonkisyonumuz değer olarak tanımlar.
x = 1
while x <= 30:
    print(fibonacci(x),end=" ")
    x += 1
