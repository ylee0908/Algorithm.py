#time : O(n), space: O(1)
def singleNumber(nums):
        
        ans = 0
        for i in nums:
            ans ^= i
        return ans
        
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
