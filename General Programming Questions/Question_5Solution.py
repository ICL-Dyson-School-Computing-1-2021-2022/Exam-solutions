'''
Question5.py

Corresponding solution file for Question5.py.

NOTE: This is only one possible solution, logically
equivalent ones also acceptable.

'''


# Write a function that, given a list of list of numbers and an integer n
# returns a dictionary with two keys: 'numbers' and 'power'.
#   - The value associated with 'numbers' is the input list of numbers,
#   - The value associated with 'power' is the n-th power of the numbers of the input list.
# for example:
# from an input list of [1,3,5,6] and n = 2
# the function will return {"numbers": [1,3,5,6], "power": [1,9,25,36]}
# WEIGHT = 5

def dictPower(listOfNumbers, pow):
    # add the power element for each element in listOfNumbers
    powers = [number**pow for number in listOfNumbers]
    dict = {"numbers": listOfNumbers, "power": powers}
    return dict

myList = [1,3,5,6]
print(dictPower(myList, 2))