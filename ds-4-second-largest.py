"""
write a program that takes a list of numbers and the second largest number in the list.
"""

def secondLargestNumber() :
    nums = [13332, 20, 11, 45, 100,3200, 384]
    large = max(nums)
    sl = 0

    for num in nums :
        if num > sl and num < large :
            sl = num
    print("Second largest number is ",sl)
secondLargestNumber()