"""
write a program that takes a string and returns the number of words in the string.
"""

def wordCount() :
    string = "write a program that takes a string and returns the number of words in the string."
    newStr = string.split(' ')
    
    print("Total words: ", len(newStr))
    
wordCount()