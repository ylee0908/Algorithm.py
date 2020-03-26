A = [-2, 1, 2, 4, 7, 11]
target = 13

#time complexity: O(n^2)
#space complexity : O(1)
def two_sum_iterative(A, target):
	for i in range(len(A)-1):
		for j in range(1, len(A)):
			if A[i] + A[j] == target:
				return A[i], A[j]
	return False

#time complexity: O(n)
#space complexity : O(n)
def two_sum_hashtable(A, target):
	d = dict()
	for i in range(len(A)):
		if A[i] in d:
			return d[A[i]], A[i]
		else:
			d[target-A[i]] = A[i]
	return False

#time complexity: O(logn)
#space complexity: O(1)
def two_sum_sorted_array(A, target):
	i = 0
	j = len(A) - 1
	while i < j:
		if A[i] + A[j] < target:
			i += 1
		elif A[i] + A[j] > target:
			j -= 1
		else:
			return A[i], A[j]
	return False


print(two_sum_iterative(A, target))
print(two_sum_hashtable(A, target))
print(two_sum_sorted_array(A, target))
