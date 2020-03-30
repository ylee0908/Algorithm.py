Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2


def findMajority(arr):
	d = {}
	for i in range(len(arr)):
		if arr[i] in d:
			d[arr[i]] += 1
		else:
			d[arr[i]] = 1

	for key in d:
		if d[key] > len(arr)// 2:
			return "Majority found :", key
			break
		else:
			return "No Majority Element"


arr = [2, 2, 2, 2, 5, 5, 2, 3, 3]

print(findMajority(arr))
