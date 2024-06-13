"""
write a program that takes a string and returns true if the string is pallindrome otherwise false.
"""

def palindrome():
    string = input("Enter your String : \n")
    # reverse = string[::-1] # predefine way to reverse the string

    reverse = ''

    for index in range(len(string)-1, -1, -1) :
        reverse = reverse + string[index]

    print(reverse)
    if reverse == string : print(string, "is palindrome")
    else : print(string, "is not palindrome")
palindrome()