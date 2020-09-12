# -*- coding: utf-8 -*-

liste1=[[1,2,3],[1,2,3],[1,2,3]]



liste2=[[3,3,3],[3,3,3],[3,3,3]]


sonuc =[[0,0,0],[0,0,0],[0,0,0]]


for x in range(0,3):
    for y in range (0,3):
        sonuc[x][y]= liste1[x][y]+liste2[x][y]
print(sonuc)
    


