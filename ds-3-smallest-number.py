"""
write a program that takes a list of numbers and the smallest number in the list.
"""

def smallestNumber() :
    nums = [23, 45, 1, 45, 45, 12, -4565, 12]
    # print(min(nums))
    small = nums[0]

    for num in nums :
        if num < small :
            small = num
    print("Smallest number is ", small)
smallestNumber()