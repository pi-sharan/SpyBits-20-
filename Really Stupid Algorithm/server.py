from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long,long_to_bytes
from secret import flag

print("Hey , Welcome to Really Stupid Algorithm Service.\n".center(100))

print("This is an untested service. We want you to test and i'll give you reward in case you find the bug.\n")

key = RSA.generate(bits=2048)

while True:


	encrypt = lambda m: pow(m,key.e,key.n)


	print("1. Encryption")
	print("2. Get the Public Key")
	print("3. Get the Encrypted Flag")
	print("4. Submit the Flag")
	print("5. Exit\n")

	try:

		type = int(input("Give me your choice now > ").strip())

		if type == 1:

			m = int(input("Give me your message > ").strip())

			print("Here's your ciphertext : 0x{:x}\n".format(encrypt(m)))

		elif type == 2:

			print("Here's the public key : n = 0x{:x} and e = 0x{:x}\n".format(key.n,key.d))

		elif type == 3:

			enc = encrypt(bytes_to_long(flag))

			print("Here's the encrypted flag : 0x{:x}\n".format(enc))

		elif type == 4:

			cipher = int(input("Give me the ciphertext different from the flag's one > ").strip())

			if cipher == encrypt(bytes_to_long(flag)):

				print("Ah!! Never do that.Get lost now !!\n")
				break


			dec = pow(cipher,key.d,key.n)

			if flag == long_to_bytes(dec):

				print("\nOk!! So there's some serious problem out there.\n")
				print("Here's your reward : {}\n".format(flag))
				break
			else:

				print("Nope!! Try harder !!\n")

		else:

			print("Wrong Choice!!\n")

	except:

		print("Some error occured. Exiting !!\n")
		break
