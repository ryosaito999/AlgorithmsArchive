def find_perm(s, temp):
	if len(s) == 1:
		output.append(temp + s[0])
		return 

	for i in s:
		find_perm(s.replace(i, ""), temp + i)



output = []
s = "abc"
find_perm(s, "")
print output