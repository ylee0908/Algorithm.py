581. Shortest Unsorted Continuous Subarray


Share
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.


Time Complexity : O(n)
Space Complexity : O(1)

Code :

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        lb = ub = -1
        lo = float('inf')
        hi = -float('inf')
        n = len(nums)
        for i in range(1,n):
            if nums[i-1] > nums[i]:
                lb = i-1
                break
        for i in range(n-2, -1, -1):
            if nums[i] > nums[i+1]:
                ub = i+1
                break
        if lb == -1 or ub == -1:
            return 0
        for i in range(lb, ub+1):
            lo = min(lo, nums[i])
            hi = max(hi, nums[i])
        
        while lb>0 and nums[lb-1] > lo:
            lb-=1
        while ub<n-1 and nums[ub+1] < hi:
            ub+=1
        return ub-lb+1
        

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        sortNums = sorted(nums)
        if sortNums == nums:
            return 0
        
        for i in range(len(nums)):
            if nums[i] != sortNums[i]:
                firstMismatchIdx = i
                break
        
        for j in range(len(nums)-1, -1, -1):
            if nums[j] != sortNums[j]:
                lastMismatchIdx = j
                break
        
        return lastMismatchIdx - firstMismatchIdx + 1
