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

c = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'.decode('hex')

single_byte_xor(c)

# flag = "Cooking MC's like a pound of bacon"

"""
Refined or Simpler Version using inbuilt tools

from pwn import xor
c = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'.decode('hex')
flag = []
for i in range(255):
	flag.append(xor(c,i))
	if "Cooking" in flag[i]:
		print flag[i]
		print i
"""
