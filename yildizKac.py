# -*- coding: utf-8 -*-

sayi = 0
kac = int(input("Kaç Yıldız: "))
yildiz=""


# while sayi < kac :
#      yildiz=yildiz + "*"
#      print(yildiz)
#      sayi = sayi +1



for kac in range (1, kac +1):
    yildiz= yildiz +"*"
    print (yildiz)
    
    
asal = int (input ("Sayi Giriniz: ")) 

liste = (2,3,4,5,6,7,8,9)

 
for x in range (2,asal):
   if  (asal % x) == 0:
       print("Bu sayi asal değildir.")
   break
print ("Bu sayi asal değildir.")
   
     
   
   