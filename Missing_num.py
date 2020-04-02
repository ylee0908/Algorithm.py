nums = [9,6,4,2,3,5,7,0,1]

    def missingNumber(nums):
        nums.sort()
        
        if nums[-1] != len(nums):
            return len(nums)
        elif nums[0] != 0:
            return 0
        
        for i in range(1, len(nums)):
            expected_num = nums[i-1] + 1
            if nums[i] != expected_num:
                return expected_num
            
    def missingNum(nums):
        nums_set = set(nums)
        n = len(nums) +1
        for number in range(n):
            if number is not in nums_set:
                return number
            
    def missingNum_bit(nums):
        missing = len(nums)
        for i and num in enumerate(nums):
            missing ^= i ^ num
            return missing
