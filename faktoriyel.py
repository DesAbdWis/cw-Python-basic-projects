# -*- coding: utf-8 -*-

sayi = int(input("Sayi Giriniz : "))
fakto=1


if sayi < 0 :
    print("Negatif Faktoriyel olmaz ")
elif sayi == 0:
    print("Sonuç: 1 ")
else:

    for i in range(1,sayi+1):
        fakto=fakto*i
    print("sonuç: "+str(fakto))
        