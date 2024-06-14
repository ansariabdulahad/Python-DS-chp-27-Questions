"""
write a program that takes a list of strings and returns True if the string contains only
alphabets.
"""

def checkAlpha() :
    string = input("Enter Input: \n")

    if string.isalpha() : print("Provided input containes only alphabets")
    else : print("Provided input does not containes only alphabets")
checkAlpha()