def faktoriyel(n):
    if n == 0: # Soruda 1'den N'ye kadar diyor ama yine de faktoriyel(0)'ı girmek istedim.
        return 1
    elif n == 1:
        return n
    else:
        return n*faktoriyel(n-1)
