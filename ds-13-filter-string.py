"""
write a program that takes a list of strings and returns a new list of strings, whose length is 
greater than or equal to 5.
"""

def filterString():
    strings = ['ass', 'ahad', 'ansari', 'samad', 'wahid', 'abc']
    newList = []

    for str in strings :
        if len(str) >= 5 :
            newList.append(str)
    print("grether then 5: ", newList)
filterString()

