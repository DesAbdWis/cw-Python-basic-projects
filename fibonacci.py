# -*- coding: utf-8 -*-

fibo_num =[1]

sum =1

for i in range(1,55):
    fibo_num.append(sum)
    sum = fibo_num[i-1]+fibo_num[i]
    if sum >55:
        break
    
print(fibo_num)


#"solution 2"

# x, y = 0, 1
# fibo = []
# while y < 56:
#     fibo.append(y)
#     x, y = y, x+y
# print(fibo)