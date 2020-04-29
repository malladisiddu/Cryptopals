'''----------------------------------<Server-Side>-------------------------------------'''
from Crypto.Cipher import AES
from Crypto.Util.number import *

# Secret values not known to the attacker
from key import AES_key, MAC_flag

AES_key = AES_key.decode('hex')
iv = '\x00' * 16
blocksize = 16

def MAC_generation(plaintext):
	try:
		assert len(plaintext) % 16 == 0

		# Doesn't allow to generate MAC of the plaintext
		if plaintext == "Check length extension attack!!!":
			print "[-]Not allowed to calculate MAC of this string!"
			exit()
		
		obj1 = AES.new(AES_key,AES.MODE_CBC,iv)
		ciphertext = obj1.encrypt(plaintext)
		ciphertext = ciphertext[len(ciphertext) - 16:]
	
		return ciphertext.encode('hex')
	except:
		print "Invalit Input"

def MAC_auth(auth_tag):
	if auth_tag == MAC_flag:
		print "[+]Successful Exploit!"
	else:
		print "[-]Exploit Failed!"
'''----------------------------------<Server-Side>---------------------------------------'''


'''---------------------------------<Attacker-Side>--------------------------------------'''


def xor_strings(s1, s2):
	assert len(s1) == len(s2)
	ct = "".join([chr(ord(s1[i]) ^ ord(s2[i])) for i in range(len(s1))])
	return ct

def exploit():
	target_string = "Check length extension attack!!!"
	assert len(target_string) == 32
	
	'''Direct check: Calling the MAC_generation function to by passing
	target_string as the parameter directly --> Not allowed by the server'''
	MAC_generation(target_string)

	# Exploit to by pass the check
	print "\n\nThe Exploit!!!"
	first_slice = target_string[:16]

	'''We are allowed to give input to the server, hence calling the
	MAC_generation function for illustration'''
	MAC_first_slice = MAC_generation(first_slice).decode('hex')
	
	second_slice = xor_strings(MAC_first_slice, target_string[16:32])
	MAC_target_string = MAC_generation(second_slice)

	MAC_auth(MAC_target_string)

if __name__ == "__main__":
	exploit()
'''--------------------------------<Attacker-Side>-----------------------------------'''
	  
