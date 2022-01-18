'''
Question2.py

Corresponding solution file for Question2.py.

NOTE: This is only one possible solution, logically
equivalent ones also acceptable.

'''


# Write a function to find the sum of all the numerical values in a list that can contain
# an arbitrary number of arbitrary types:
# for example:
# from an input list of ["hello", "cat", 2, True, 17, None]
# the function will return 19
# WEIGHT = 4

def sumOfNumbers(listOfStuff):
    sum = 0
    counter = 0
    for element in listOfStuff:
        # check if the element is an int or a float and sum them to the previous value
        # the counter checks how many elements the sum went over. If the number is zero, 
        # it means that there were no elements and the function returns None
        if type(element) is int or type(element) is float:
            sum += element
            counter += 1
    if counter > 0:
        return sum
    else:
        return None

myList = ["hello", "cat", 2, True, 17, None, -12.4]
print(sumOfNumbers(myList))