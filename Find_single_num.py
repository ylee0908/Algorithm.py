Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
# time: O(n), space: O(n)

    #time : O(n), space: O(1)
    def singleNumber(nums):

        ans = 0
        for i in nums:
            ans ^= i
        return ans
    def singleNumber(nums):
        ht = dict()
        for i in nums:
            if i in ht:
                ht[i] = 1
            else:
                ht[i] += 1
        for i in ht:
            if ht[i] == 1
            return i

#time/space: O(n)
def SingleNumber(nums):
	d = dict()
	for i in nums:
		if i in d:
			d[i] += 1
		else:
			d[i] = 1
	for i in d:
		if d[i] == 1:
			return i



nums= [2, 2, 1]
print(SingleNumber(nums))
