"""
write a program that takes a list of numbers and returns the sum of all the numbers.
"""

def listSum() :
    nums = [2, 4, 1, 4, 2]
    sumOfAll = 0

    for num in nums :
        sumOfAll = sumOfAll + num
    
    print("Sum of all numbers: ", sumOfAll)
listSum()