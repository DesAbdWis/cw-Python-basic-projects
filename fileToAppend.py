# -*- coding: utf-8 -*-

ogrenciler = ["Ahmet", "Ayşe", "Arda", "Hilal"]

fileToAppend = open("ogrenciler.txt", "a", encoding="utf-8")

for ogrenci in ogrenciler:
    fileToAppend.write(ogrenci)
    fileToAppend.write("\n")
    
    
fileToAppend = open("ogrenciler.txt", "r", encoding="utf-8")
print(fileToAppend.read())
    
    
    
fileToAppend.close()