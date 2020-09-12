# -*- coding: utf-8 -*-

print("Operasyon?")
print("1: topla")
print("2: çıkar")
print("3: çarp")
print("4: böl")

operasyon= int(input("Giriniz: "))
sayi1 =int (input("1.sayı giriniz: "))
sayi2 =int (input("2.sayı giriniz: "))


# class hesapMakinesi():
#     def __init__(self,sayi1,sayi2):
#         self.sayi1=sayi1
#         self.sayi2=sayi2
        
#     def topla(self,sayi1,sayi2):
#        return print(self.sayi1+self.sayi2)
#     def cikar(self,sayi1,sayi2):
#         return print(self.sayi1-self.sayi2)   
#     def carp(self,sayi1,sayi2):
#         return print(self.sayi1*self.sayi2)
#     def bolme(self,sayi1,sayi2):
#         return print(self.sayi1/self.sayi2)
        
  

      
# if operasyon==1:
#     hesapMakinesi.topla(self,sayi1,sayi2)
# elif operasyon==2 :
#     hesapMakinesi.cikar(sayi1, sayi2)
# elif operasyon==3 :
#     hesapMakinesi.carp(sayi1, sayi2) 
# elif operasyon==4:
#     hesapMakinesi.bolme(sayi1, sayi2)
# else:
#     print("Lütfen sadece 1-2-3-4 rakamları giriniz")
    
# print(matematik())
    
def topla(sayi1,sayi2):
    return sayi1+sayi2
def cikar(sayi1,sayi2):
    return sayi1-sayi2
def carp(sayi1,sayi2):
    return sayi1*sayi2
def bolme(sayi1,sayi2):
    return sayi1/sayi2


if operasyon==1:
    print("toplam: ",topla(sayi1, sayi2))
elif operasyon==2 :
   print("fark: ",cikar(sayi1, sayi2))
elif operasyon==3 :
   print("sonuç: ",carp(sayi1, sayi2)) 
elif operasyon==4:
    print("sonuç: ", bolme(sayi1,sayi2))
else:
    print("Lütfen sadece 1-2-3-4 rakamları giriniz")