"""
write a program that takes a list of strings and returns a new list that contains only more than one
words.
"""

def moreThanOneWord() :
    strings = ['ahad', 'ahad ansari', 'samad', 'noor ansari', 'wahid ansari', 'just for code']
    newStr = []

    for str in strings :
        length = str.split(' ')
        if len(length) > 1 : newStr.append(str)
    
    print("more than one word:", newStr)
    
moreThanOneWord()