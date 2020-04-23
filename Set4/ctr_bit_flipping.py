from Crypto.Cipher import AES
from Crypto.Util import Counter
from os import urandom
import binascii

key = urandom(16)
iv = urandom(16)

def int_of_strings(s):
	return int(binascii.hexlify(s), 16)
def padding(m):
	pad_len = 16 - len(m) % 16
	m_hex = m.encode('hex') + pad_len*(hex(pad_len)[2:].zfill(2))
	return m_hex.decode('hex')
def ctr_encrypt(payload):
	for i in range(len(payload)):
		if payload[i] == '=':
			payload = payload.replace(payload[i],'?')
	string = "comment1=cooking%20MCs;userdata=" + payload + ";comment2=%20like%20a%20pound%20of%20bacon"
	string = padding(string)
	ctr = Counter.new(128, initial_value = int_of_strings(iv))
	obj = AES.new(key,AES.MODE_CTR, counter=ctr)
	ct = obj.encrypt(string)
	return ct
def ctr_decrypt(ct):
	ctr = Counter.new(128, initial_value = int_of_strings(iv))
	obj1 = AES.new(key,AES.MODE_CTR, counter=ctr)
	pt = obj1.decrypt(ct)
	if "admin=true" in pt:
		print "You are admin now"
	else:
		print "You need to get the Admin access"

cipher_list = []
payload = "admin=true"
ct = ctr_encrypt(payload)

for k in range(len(ct)/16):
	cipher_list.append(ct[16*k : 16*(k+1)])
block = list(cipher_list[2])
block[6] = chr(ord(block[6]) ^ ord('?') ^ ord('='))
cipher_list[2] = ''.join(block)
ct = ''.join(cipher_list)

ctr_decrypt(ct)


