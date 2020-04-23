from Crypto.Cipher import AES
from os import urandom

key = urandom(16)
iv = urandom(16)

def padding(pt,blocksize):
	pad_len = (16 - len(pt) % 16)
	pt_hex = pt.encode('hex') + pad_len*(hex(pad_len)[2:].zfill(2))
	return pt_hex.decode('hex')
def cbc_encrypt(pt):
	pt = padding(pt,16) 
	obj1 = AES.new(key,AES.MODE_CBC,iv)
	return obj1.encrypt(pt)
def cbc_decrypt(ct):
	obj2 = AES.new(key,AES.MODE_CBC,iv)
	ct = obj2.decrypt(ct)
	return ct
#-------------------------------------server side----------------------------------
#------------------------------------attacker's side---------------------

pt = "Malladi Siddartha is the CEO and Founder of Zsquare , Zeal and Zenith".encode('hex')
ct = cbc_encrypt(pt)
ct = ct[:16] + '\x00' * 16 + ct[:16]
pt1 = cbc_decrypt(ct)

possible_iv = ""

for i in range(16):
	possible_iv += chr(ord(pt1[i]) ^ ord(pt1[32+i]))
print possible_iv == iv

if possible_iv == iv:
	print "Exploit is working. possible iv: ", possible_iv.encode('hex')
else:
	print "Exlpoit isn't working"
