'''
Question6.py

Corresponding solution file for Question6.py.

NOTE: This is only one possible solution, logically
equivalent ones also acceptable.

'''


# Write a function that accepts two string as inputs. 
# The first parameter will be a string of characters, and the second parameter 
# will be the same string of characters, but they will be in a different order 
# and have one extra character. The function should return that extra character.
#   - if the strings differ for more than two characters the function will return None
# for example:
# from inputs: "hello", "hollen"
# the function will return "n"
# from inputs: "hello", "hollenn"
# the function will return None
# WEIGHT = 5

def missingWord(string1, string2):
    # we remove elements from string2 until we are left with only one element. 
    # notice that the additional letter might be one that is also present in string1, just repeated twice
    if len(string2) - len(string1) == 1:
        listString2 = list(string2)                
        for letter in string1:               
            if letter in listString2:      
                listString2.remove(letter)   
        if len(listString2) == 1:              
            return listString2[0]
        else: 
            return None
    else:
        return None
string1 = "hello"
string2 = "lholeo"
print(missingWord(string1, string2))