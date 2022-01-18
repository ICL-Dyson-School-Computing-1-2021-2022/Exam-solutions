'''
Question1.py

Corresponding solution file for Question1.py.

NOTE: This is only one possible solution, logically
equivalent ones also acceptable.

'''


# Write a function to find the shortest word from a list of words:
# for example:
# from an input list of ["hello", "cat", "ok", "12345"]
# the function will return "ok"
# WEIGHT = 2



def shortestWord(words):
    # check for the shortest word starting from the first one. 
    shortestLength = len(words[0])
    shortestIndex = 0
    for index, word in enumerate(words):
        length = len(word)
        if length < shortestLength:
            # if the new word is shorter, override the previous one
            shortestLength = length
            shortestIndex = index
    return words[shortestIndex]


l = ["hello", "cat", "ok", "12345", "1"]
print(shortestWord(l))  
