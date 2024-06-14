"""
write a program that takes a list of numbers and returns new list with numbers that are devisible
by 3.
"""

def divisible() :
    nums = []
    newList = []

    for index in range(5) :
        try : num = int(input("Enter a number: \n"))
        except : raise Exception("Invalid Input !")
        else :
            nums.append(num)
    
    for num in nums :
        if num % 3 == 0 :
            newList.append(num)
    
    print("Divisible by threee", newList)
divisible()