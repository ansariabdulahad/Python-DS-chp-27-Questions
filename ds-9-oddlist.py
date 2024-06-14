"""
write a program that takes a list of numbers and returns an odd numbers in new list.
"""

def oddList() :
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    odd = []

    for num in nums :
        if num % 2 != 0 :
            odd.append(num)
    
    print("Odd numbers are", odd)
oddList()