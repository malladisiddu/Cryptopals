from Crypto.Cipher import AES
def encrypts(testinput):
	secret="Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK".decode('base64')
	
	message = testinput + secret
	message += (16-len(message)%16) * chr(16-len(message)%16)
	k = "YELLOW SUBMARINE"
	key = AES.new(k,AES.MODE_ECB)
	ct = key.encrypt(message)
	return ct
 


flag=""
for k in range(1,10):	
	for j in range(15,-1,-1):
		testinput = j * 'A'
		block = encrypts(testinput)
		for i in range(256):
			op_block = encrypts(testinput + flag + chr(i))
			if (op_block[:16*k] == block[:16*k]):
				flag+=chr(i)
				break
print flag
