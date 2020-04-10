def fixed_xor(a,b):
	flag = ""
#xoring two equal length strings
	for i in range(len(a)):
		flag +=hex(ord(a[i]) ^ ord(b[i]))[2:]
	print 'flag is : ',flag
	return 0
a = '1c0111001f010100061a024b53535009181c'.decode('hex')
b = '686974207468652062756c6c277320657965'.decode('hex')
fixed_xor(a,b)
