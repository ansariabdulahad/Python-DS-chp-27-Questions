"""
write a program that takes a list of numbers and returns a new list with prime numbers.
"""

def primeList() :
    nums = [12, 345, 13, 15, 1, 3, 7, 11, 19, 32, 45, 56, 12, 6, -23, -23, 12,44]
    primeList = []

    for num in nums :
        if num > 1 :
            for index in range(2, num) :
                if num % index == 0 :
                    break
            else :
                primeList.append(num)
    
    print("Prime list is :", primeList)
primeList()