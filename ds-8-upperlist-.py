"""
write a program that takes a list of strings and returns a new list of strings in uppercase.
"""

def upperList() :
    strings = ['ahad', 'noor','samad', 'wahid']
    uppercaseString = []

    for str in strings :
        uppercaseString.append(str.upper())
    
    print("Uppercase string", uppercaseString)
upperList()