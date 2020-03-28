def array_advance(A):
    furthest_reached = 0
    last_idx = len(A) - 1
    i = 0
    while i <= furthest_reached and furthest_reached < last_idx:
        furthest_reached = max(furthest_reached, A[i] + i)
        i += 1
    return furthest_reached >= last_idx


# True: Possible to navigate to last index in A:
# Moves: 1,3,2
A = [3, 3, 1, 0, 2, 0, 1]
print(array_advance(A))

# False: Not possible to navigate to last index in A:
A = [3, 2, 0, 0, 2, 0, 1]
print(array_advance(A))

A1 = [1, 4, 9]
A2 = [9, 9, 9]

# s = ''.join(map(str, A))
# print(int(s) + 1)


def plus_one(A):
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i-1] += 1
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A


print(plus_one(A1))
print(plus_one(A2))

A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]


# Time Complexity: O(n^2)
# Space Complexity: O(1)
def buy_and_sell_once(A):
	max_profit = 0
	for i in range(len(A) - 1):
		for j in range(i + 1, len(A)):
			if A[j] - A[i] > max_profit:
				max_profit = A[j] - A[i]
	return max_profit


# Time Complexity: O(n)
# Space Complexity: O(1)
def buy_and_sell_stock_once(prices):
	# Check if the prices array is less than 2
	if len(prices) < 2:
		return 0

	min_price = prices[0]
	max_profit = 0

	for price in prices:
		min_price = min(min_price, price)
		compare_profit = price - min_price
		max_profit = max(max_profit, compare_profit)

	return max_profit
