'''
Question4.py

Corresponding solution file for Question4.py.

NOTE: This is only one possible solution, logically
equivalent ones also acceptable.

'''


# Write a function that, given two integer inputs a and b (with b > a), returns a list of
# all the numbers between a and b (a and b included) whose square root is an integer.
# for example:
# from inputs 2 and 16
# the function will return [4, 9, 16]
# WEIGHT = 5

def perfectSquares(a, b):
    listofPerfectSquares = []
    for number in range(a,b+1, 1):
        sqrt = number**0.5
        if sqrt % 1 == 0:
            # if the remainder of the division by 1 is 0, sqrt belongs to the integers
            listofPerfectSquares.append(number)
    return listofPerfectSquares

print(perfectSquares(2,16))