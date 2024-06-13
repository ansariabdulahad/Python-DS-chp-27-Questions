"""
write a program that takes a string and returns a number of vowels..
"""

def vowelCount() :
    vowels = 'aeiou'
    string = input("Enter your string \n")
    count = 0

    for char in string :
        if char.lower() in vowels :
            count = count + 1
    print("Total vowels are:", count)
vowelCount()