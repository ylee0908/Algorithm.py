n = 5

def fibonacci(n):
	if n < 0:
		return None
	elif n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(n))
