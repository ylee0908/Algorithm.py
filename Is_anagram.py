#Anagram: rearrange letters but needs to have a meaning

s1 = "fairy tales"
s2 = "rail safety"

#sorted is O(nlogn) in time complexity.
def is_anagram_sorted(s1, s2):
	s1 = s1.replace(" ", "").lower()
	s2 = s2.replace(" ", "").lower()

	return sorted(s1) == sorted(s2)

#time complexity: O(n)

def is_anagram_ht(s1, s2):
	ht = dict()

	if len(s1) != len (s2):
		return False

	for i in s1:
		if i in ht:
			ht[i] += 1
		else:
			ht[i] = 1
	for i in s2:
		if i in ht:
			ht[i] -= 1
		else:
			ht[i] = 1
	for i in ht:
		if ht[i] != 0:
			return False
	return True


print(is_anagram_sorted(s1, s2))
print(is_anagram_ht(s1, s2))
