# -*- coding: utf-8 -*-

# class Matematik:
#     def topla(sayi1,sayi2):
#         print( "Toplam: ", sayi1+sayi2)
#     def cikar(sayi1,sayi2):
#         print( "Toplam: ", sayi1-sayi2)
#     def carp(sayi1,sayi2):
#         print( "Toplam: ", sayi1*sayi2)
#     def bol(sayi1,sayi2):
#         print( "Toplam: ", sayi1/sayi2)
        
        
# matematik = Matematik()

# matematik.topla(3,5)

class Matematik:
    def __init__(self,sayi1,sayi2):
        self.sayi1=sayi1
        self.sayi2=sayi2
        
    def topla(self,sayi1,sayi2):
        print( "Toplam: ", sayi1+sayi2)
    def cikar(self,sayi1,sayi2):
        print( "Toplam: ", sayi1-sayi2)
    def carp(self,sayi1,sayi2):
        print( "Toplam: ", sayi1*sayi2)
    def bol(self,sayi1,sayi2):
        print( "Toplam: ", sayi1/sayi2)
        
        
matematik = Matematik(1,1)

matematik.bol(2,8)


