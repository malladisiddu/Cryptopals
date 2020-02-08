import codecs
from string import ascii_uppercase as chars
a = codecs.decode(input(),'hex').decode('utf-8')
b = ""

for i in chars:
	for j in range(len(a)):
		b += chr(ord(a[j]) ^ ord(i))
print(b)
