#Program to find Anagram
def anagram(s1,s2):
	if len(s1)!=len(s2):
		False
	else:
		if sorted(s1.lower())==sorted(s2.lower()):
		    True
		else:
		    False
print(anagram("Listen","Silent"))

