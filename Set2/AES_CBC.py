from Crypto.Cipher import AES

def aes_cbc(ciphertext,key,iv):
# Using in built modules
	cipher = AES.new(key,AES.MODE_CBC,iv)
# Decrypting the cipher text into plaintext
	plaintext =  cipher.decrypt(ciphertext)
	return plaintext
key = 'YELLOW SUBMARINE'
blocksize = 16
iv = '\x00' * blocksize
ct = open('10.txt')
ciphertext = (ct.read()).decode('base64')
flag = aes_cbc(ciphertext,key,iv)
print 'Flag is: ',flag
