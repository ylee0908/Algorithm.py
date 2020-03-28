A = [7,8,5,4,9,2]

def insertion_sort(A):
	for i in range(len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break
	return A


def insertion_sort_while(A):
	for i in range(1, len(A)):
		j = i - 1
		while A[j] > A[j+1] and j>=0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1
	return A


def bubblesort(A):
	for i in range(len(A)-1):
		for j in range(len(A)-1-i):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break
	return A


print(insertion_sort(A))
print(insertion_sort_while(A))
print(bubblesort(A))
