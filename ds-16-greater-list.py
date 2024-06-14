"""
write a program that takes a list of numbers and returns only the numbers that are even and 
greater than 10.
"""

def greaterList():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    for num in nums :
        if num % 2 == 0 and num > 10 :
            print("Greater than 10 and even numbers :", num)
greaterList()