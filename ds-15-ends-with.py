"""
write a program that takes a list of strings and returns a new list with all the letters that
ends with the letter "s".
"""

def endWith():
    strings = ['books', 'laptop', 'mouses', 'speakers']
    newList = []
    sletters = []

    for str in strings :
        if str.endswith('s') :
            newList.append(str)
        
        lastLetter = str[len(str) - 1]
        if lastLetter.lower() == 's' :
            sletters.append(str)
    print("Ends with s: ", sletters)
endWith()