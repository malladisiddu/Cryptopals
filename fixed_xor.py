import codecs
a = codecs.decode(input(),"hex").decode('utf-8')
b = codecs.decode(input(),"hex").decode('utf-8')
print(a)
print(b)
for i in range(len(a)):
	print(hex(ord(a[i])^ord(b[i]))[2:],end= "")
