"""
write a program that takes a list of numbers and returns a new list with only perfect square.
"""
# int(a**0.5)**2 -- perfect square formula

def perfectSquare() :
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
    newList = []

    for num in nums :
        if int(num**0.5)**2 == num : newList.append(num)
    print(newList)
perfectSquare()