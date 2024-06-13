"""
write a program that takes a list of numbers and the largest number in the list.
"""

def largestNumber() :
    nums = [12, 4, 4, 54, 56, 23, 65, 76, 88, 45]
    # print(max(nums))
    large = nums[0]
    for num in nums :
        if num > large :
            large = num
    print("Large number is : ", large)
largestNumber()