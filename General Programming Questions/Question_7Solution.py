'''
Question7.py

Corresponding solution file for Question7.py.

NOTE: This is only one possible solution, logically
equivalent ones also acceptable.

'''


# Write a function that accepts two integers as an input. The function will return
# a list of all the numbers n between a and b (a and b included), such that every digit in n is even.
# for example:
# given as inputs  a = 2, b = 27
# the function will return [2, 4, 6, 8, 20, 22, 24, 26] 
# notice that, for instance in 14, 1 is odd and 4 is even, therefore 14 is not added to the list
# WEIGHT = 8

def areDigitsEven(n):
    # check digit by digit if the digit is even
    strNumber = str(n)
    for digit in strNumber:
        if int(digit) % 2:
            return False
    return True

def evenDigits(a, b):
    # apply the previous function to all the numbers between a and b
    listOfNumbers = []
    for number in range(a,b+1):
        if areDigitsEven(number):
            listOfNumbers.append(number)

    return listOfNumbers

print(evenDigits(2,50))




