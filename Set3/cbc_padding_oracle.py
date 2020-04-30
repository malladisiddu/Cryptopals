from Crypto.Cipher import AES
from os import urandom
import random

key = urandom(16)

def pad_check(string, block=16):
	pad = string[len(string)-1]
	if pad == '\x00':
		return False
	intpad = ord(pad)
	try:
		for i in range(intpad):
			if string[::-1][i] != pad:
				raise
		string = string.rstrip(pad)
		return True
	except:
		return False
 
	
def xor(a,b):
	return ''.join(chr(ord(i) ^ ord(j)) for i,j in zip(a,b))

def xor_3(a,b,c):
	return ''.join(chr(ord(i) ^ ord(j) ^ ord(k)) for i,j,k in zip(a,b,c))

def encrypt():
	t = open('17.txt').readlines()
	
	pt = t[9].rstrip('\n').decode('base64')
	print pt
	pad = 16 - len(pt) % 16
	pt += pad * chr(pad)
	iv = urandom(16)
	obj = AES.new(key,AES.MODE_CBC,iv)
	ct = obj.encrypt(pt)
	return [ct,iv]

def decrypt(ct,iv):
	obj = AES.new(key,AES.MODE_CBC,iv)
	pt = obj.decrypt(ct)
	return pad_check(pt)

def exploit():
	# takes the list output
	output = encrypt()
	
	ct = output[0]
	iv = output[1]
	
	# to get the number of blocks (involves iv)
	
	nblock = len(ct)/16 + 1
	block_size = 16

	# to break the ct into ct list
	
	ct_list = [iv]
	pt_list = []
	for i in range(nblock):
		ct_list += [ct[i*block_size : (i+1)*block_size]]	
	flag = ""
	for i in range(nblock-1 , -1, -1):
		
		# to create 1 block attack
		brute = '\x00' * block_size
		pt_block = ""
		for j in range(15,-1,-1):
			pad = chr(16 - j)
			for k in range(256):
				mod = xor_3(ct_list[i-1],'\x00'*j + pad * (16-j), brute[:j]+chr(k) + pt_block)
				att = mod + ct_list[i]
				print "mod: ",len(brute[:j]+chr(k)+pt_block)
				if decrypt(att,iv):
					print chr(k)
					pt_block = chr(k) + pt_block
					
		flag = pt_block + flag
		print "--------"
	print flag

if __name__ == "__main__":
	exploit() 

