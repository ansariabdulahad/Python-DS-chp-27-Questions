"""
write a program that takes a list of numbers and returns a new list that are odd and less then 5.
"""

def smallerList():
    nums = [0, -1, -2, -3, -4, -5, -6, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    newList = []

    for num in nums:
        if num % 2 != 0 and num < 5 :
            newList.append(num)
    
    print("less and odd numbers: ", newList)
smallerList()