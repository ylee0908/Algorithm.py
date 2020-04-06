nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
#hashset function
#time : O(n) for nums_set and loop
#space: O(n) for set function
def missing_num(nums):
    nums_set = set(nums)
    n = len(nums) + 1
    for i in range(n):
        if i not in nums:
            return i

print(missing_num(nums))

# time: O(n) due to sum function
# space: O(1)
def missingNum(nums):
    expected_sum = (len(nums) * (len(nums)+1)) // 2
    actual_sum = sum(nums)
    missing_num = expected_sum - actual_sum

    return missing_num

print(missingNum(nums))

#time: O(n)
#space: O(1)
def missing_num_bit(nums):
    missing = len(nums)
    for i, n in enumerate(nums):
        missing ^= i ^ n
    return missing

print(missing_num_bit(nums))
