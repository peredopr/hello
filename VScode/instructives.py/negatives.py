#1st way
def count_negatives(nums):
    return sum([num < 0 for num in nums])

nums = [5, -1, -2, 0, 3]
print(count_negatives(nums))


#2nd way
def count_negatives2(nums):
    return len([num for num in nums if num < 0])

print(count_negatives2(nums))