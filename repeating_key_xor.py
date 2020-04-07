def repeating_key_xor(plaintext,key):
#xoring repeatingly with the key
#First byte of the plaintext with first byte of the key
#Second byte of the plaintext with second byte of the key
#Third byte of the plaintext with third byte of the key
#And again fourth byte of the plaintext with first byte of the key and so on... 	
	flag = ''
	i = 0
	for j in plaintext:
		flag += chr(ord(j) ^ ord(key[i]))
		if i+1 == len(key):
			i = 0
		else:
			i += 1
	return flag

key = 'ICE'
plaintext = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
ciphertext = repeating_key_xor(plaintext,key)
print "Flag is: ",ciphertext.encode('hex')
