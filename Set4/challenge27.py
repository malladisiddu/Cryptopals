from Crypto.Cipher import AES
from os import urandom

key = urandom(16)
iv = key

def padding(m,blocksize):
	pad_len = blocksize - len(m) % blocksize
	m_hex = m.encode('hex') + pad_len*(hex(pad_len)[2:].zfill(2))
	return m_hex.decode('hex')
def encrypts(pt):
	pt = padding(pt,16)
	obj = AES.new(key,AES.MODE_CBC,iv)
	ct = obj.encrypt(pt)
	return ct
def decrypts(ct):
	obj1 = AES.new(key,AES.MODE_CBC,iv)
	pt = obj1.decrypt(ct)
	return pt
pt = "flag{This is a test to check if the attack works or not!!!!}"
pt = padding(pt,16)
ct = encrypts(pt)
ct = ct[:16] + '\x00' * 16 + ct[:16]
pt1 = decrypts(ct)
possible_iv = ""
for i in range(16):
	possible_iv += chr(ord(pt1[i]) ^ ord(pt1[32+i]))
print possible_iv == iv

if possible_iv == iv:
	print "The possible iv: ", possible_iv.encode('hex')
else:
	print "Exlpoit isn't working"

key1 = possible_iv

