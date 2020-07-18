from string import ascii_uppercase as chars
def single_byte_xor(a):
#xoring with single byte when input is hex encoded string
	flag = ''
	for i in chars:
		for j in range(len(a)):
			flag += chr(ord(a[j]) ^ ord(i))
		if 'Cooking' in flag:
			print flag
			print 'XORed with byte: ',i
			break
	return None

a = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'.decode('hex')

single_byte_xor(a)
