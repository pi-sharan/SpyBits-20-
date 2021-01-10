from Crypto.Cipher import AES
from Crypto.Util.number import *
from Crypto.Random import *
from secret import flag

print("Welcome to the Super Secure Service. We are very serious about security and will give the decryption only when it is seems authentic. Try your hand.")

key1 = get_random_bytes(16)

cipher = AES.new(key1, AES.MODE_CBC , iv = b"\x00"*AES.block_size )

key2 = get_random_bytes(16)



def encryptAndSign(m):

	cipher = AES.new( key1, AES.MODE_CBC, iv = b"\x00" * AES.block_size )

	sign =  AES.new(key2, AES.MODE_CBC, iv = b"\x00" * AES.block_size )

	return cipher.encrypt(m),sign.encrypt(m)[-16:]

def decrypt(c):

	cipher = AES.new( key1, AES.MODE_CBC, iv = b"\x00" * AES.block_size )

	return cipher.decrypt(c)



pad = lambda m : m + b"\x00"*( 16 - len(m)%16 )


flagEnc , flagMac = encryptAndSign( pad(flag) )



while True:

	print("\n1. Encrypt")
	print("2. Decrypt and Verify")
	print("3. Get flag")
	print("4. Exit\n")

	try:

		type = int(input("Give your choice now > ").strip())

		if type == 1:

			m = input("Tell me which message you want to secure in hex format > ").strip()

			assert len(m)%2 == 0

			m = bytes.fromhex(m)

			if len(m)%16: m = pad(m)

			enc , mac = encryptAndSign(m)

			print("Get em here : enc = {} and mac = {}".format( enc.hex(), mac.hex() ) )

		elif type == 2:

			enc = input("Tell me your ciphertext in hex format > ").strip()

			mac = input("Tell me your mac in hex format > ").strip()

			enc = bytes.fromhex(enc); mac = bytes.fromhex(mac)

			assert len(enc)%16 == 0 and len(mac) % 16 == 0

			m  = decrypt(enc)

			hash = encryptAndSign(m)[1]

			if enc == flagEnc and mac == flagMac:

				print("You are not that smart.Get lost.")
				break

			elif hash == mac :

				print("Authentic Message. Here's your plaintext : {}".format( m.decode("latin-1") ) )

			else:

				print("You must messed up something with the mac or ciphertext. Not authentic :(.")

		elif type == 3:

			print("Here's your the secret = {} and hash = {}".format( flagEnc.hex() , flagMac.hex() ) )

		else:

			print("Ok. Bye. HF\n")
			break

	except:
		print("Something must have gone very bad :(. Exiting\n")
		break

