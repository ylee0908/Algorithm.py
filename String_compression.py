str_1 = "aabcccccaaa"
str_2 = "aaaaaabbccbcaabb"


def compression_string(s):
	comp = ""
	count = 1
	for i in range(len(s)-1):
		if s[i] == s[i+1]:
			count += 1
		else:
			comp += s[i] + str(count)
			count = 1
	comp += s[i] + str(count)
	if len(comp) >= len(s):
		return str
	else:
		return comp




print(compression_string(str_1))
print(compression_string(str_2))
