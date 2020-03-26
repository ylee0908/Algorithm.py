n = 5

def factorial_iterative(n):
	x = 1
	for i in range(n, 0, -1):
		x *= i
	return x


def factorial_recursive(n):
	if n <= 1:
		return 1
	else:
		return n * factorial_recursive(n-1)


print(factorial_iterative(n))
print(factorial_recursive(n))
