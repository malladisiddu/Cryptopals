from string import ascii_uppercase as chars
ciphers =  open('4.txt').read().splitlines()
result = ''
for hexstring in ciphers:
	ciphertext = hexstring.decode('hex')
for i in ciphertext:
	for j in chars:
		for k in range(len(ciphertext)):
			result += chr(ord(ciphertext[k]) ^ ord(j))
		print result

			

				
