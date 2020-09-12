# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 12:44:23 2020

@author: aydogdu
# """


# number = int(input("Input a Positive Integer number: "))

# n=number // = 10
# print(n)



# # # initialize sum
# # sum = 0

# # # find the sum of the cube of each digit
# # temp = number
# # while temp > 0:
# #    digit = temp % 10
# #    sum += digit ** 3
# #    temp //= 10

# # # display the result
# # if number == sum:
# #    print(number,"is an Armstrong number")
# # else:
# #    print(number,"is not an Armstrong number")

# def my_function (a,b)
#     area = a*b
#     print(my_function(3,4))

number = input("Enter a number: ")
if number.isnumeric() :
    sum = 0
    num = int(number)
    temp = num
    while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10
    if num == sum:
       print(num,"is an Armstrong number")
    else:
       print(num,"is not an Armstrong number")
else :
     print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
