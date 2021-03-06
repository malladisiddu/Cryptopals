from Crypto.Cipher import AES
from Crypto.Util.number import *
from os import urandom
from secret import flag

BLOCKSIZE = 16
key = urandom(16)
print "key: ", key.encode("hex")
iv = urandom(16)
print "iv: ", iv.encode("hex")

def pad(s):
	s += (BLOCKSIZE - (len(s) % BLOCKSIZE))*(chr(BLOCKSIZE - (len(s) % BLOCKSIZE)))
	return s

def encryption(plaintext):
	plaintext = plaintext + flag
	plaintext = pad(plaintext)
	assert len(plaintext) % BLOCKSIZE == 0
	obj1 = AES.new(key, AES.MODE_CBC, iv)
	ciphertext = obj1.encrypt(plaintext)
	return ciphertext.encode("hex")

#<----------------------------------</Server-Side>----------------------------------->
#<----------------------------------<Attacker's-Side>-------------------------------->
s = ""
for k in range(4):
	for i in range(1, BLOCKSIZE+1):
		input_str = 'a'*(16-i)
		ct = encryption(input_str)[32*k:32*k+32]
		for j in range(256):
			ct1 = encryption(input_str + s + chr(j))[32*k:32*k+32]
			if ct == ct1:
				s += chr(j)
				break
		print s
