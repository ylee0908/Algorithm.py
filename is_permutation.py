#time complexity : O (n log n)
#space complexity : O(n)
def is_permutation_one(str_1, str_2):
	str_1 = str_1.lower().replace(" ", "")
	str_2 = str_2.lower().replace(" ", "")

	if len(str_1) != len(str_2):
		return False

	str_1 = sorted(str_1)
	str_2 = sorted(str_2)

	for i in range(len(str_1)):
		if str_1[i] != str_2[i]:
			return False
	return True

#hash table
#time complexity : O(n)
#space complexity : O(1)
def is_permutatin_two(str_1, str_2):
	str_1 = str_1.lower().replace(" ", "")
	str_2 = str_2.lower().replace(" ", "")

	if len(str_1) != len(str_2):
		return False

	d = {}

	for i in str_1:
		if i in d:
			d[i] += 1
		else:
			d[i] =1
	for i in str_2:
		if i in d:
			d[i] -= 1
		else:
			d[i] = 1
	return all(value == 0 for value in d.values())


#time complexity : O(n)
#space complexity : O(1)
def is_permutation_three(str_1, str_2):
	str_1 = str_1.lower().replace(" ", "")
	str_2 = str_2.lower().replace(" ", "")


	if len(str_1) != len(str_2):
		return False

	for i in str_1:
		if i in str_2:
			str_2 = str_2.replace(i, "")
	return len(str_2) == 0


str_1 = "Google e"
str_2 = "Oogglee"

print(is_permutation_one(str_1, str_2))
print(is_permutatin_two(str_1, str_2))
print(is_permutation_three(str_1, str_2))
