"""
write a program that takes a list of strings and returns new list that starts with letter "a".
"""

def startsWith() :
    strings = ['ahad', 'abnoor', 'samad', 'wahid', 'mumtaaz']
    newList = []
    blist = []

    for str in strings :
        if str.startswith('a') :
            newList.append(str)
        
        if str[1].lower() == 'b' :
            blist.append(str)
    
    print("List that starts with letter a :", newList)
    print("List that starts with letter b :", blist)
startsWith()