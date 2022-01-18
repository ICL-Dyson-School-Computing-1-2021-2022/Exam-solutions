'''
Question3.py

Corresponding solution file for Question3.py.

NOTE: This is only one possible solution, logically
equivalent ones also acceptable.

'''


# Write a function that finds the longest palindrome in a list of words.
#   - if there is no palindrome word in the input list, the function will return None.
#   - if there are two or more palindrome words of the same length, return the first one in the list.
# Ignore punctuation and upper and lower cases. 
# Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward
# for example:
# from an input list of ["cat", "hello", "nun"]
# the function will return "nun"
# from an input list of ["cat", "hello", "nun", "never odd or even"]
# the function will return "never odd or even"
# WEIGHT = 8

def isPalindrome(word):
    # invert the word and remove spaces. if the inverted word and the normal word are the same, the word is a palindrome
    normalWord = [letter for letter in word if letter != " "]
    reversedWord = [letter for letter in word[len(word) - 1::-1] if letter != " "]
    if normalWord == reversedWord:
        return True
    else:
        return False


def longestPalindrome(listOfWords):
    # check for the shortest word starting from the first one. 
    length = 0
    longestPalindrome = None
    for word in listOfWords:
        if isPalindrome(word) and len(word) > length:
            # if the new word is longer, override the previous one
            length = len(word)
            longestPalindrome = word

    return longestPalindrome


myList = ["cat", "hello", "nun", "never odd or even"]
print(longestPalindrome(myList))