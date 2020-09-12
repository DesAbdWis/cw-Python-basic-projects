# -*- coding: utf-8 -*-

sayi = int (input("Sayi Giriniz: "))

asalMi ="Evet"

for x in range (2,sayi):
    if (sayi % x ) ==0:
        asalMi ="Hayır"
        break

if asalMi =="Hayır":
    print("ASAL DEĞİL")
else: 
    print("ASAL")
    
    