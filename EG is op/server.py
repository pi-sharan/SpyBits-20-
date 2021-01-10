from Crypto.PublicKey import ElGamal
from Crypto import Random
from Crypto.Util.number import *
from secret import flag


print("Welcome to my ElGamal Service. Here you can get your messages encrypted super secure for sharing. Never easy to break though.\n")
print("Due to limited time, I'll allow only limited encryptions.\n")

encryptions = 0

key = ElGamal.generate(256,Random.new().read)

p = int(key.p)
g = int(key.g)
y = int(key.y)

while True:

	encrypt = lambda m,r : ( pow(g,r,p) , m * pow(y,r,p) % p )

	print("1. Encryption")
	print("2. Get encrypted Flag")
	print("3. Exit\n")

	try:

		type = int(input("Give me your choice > ").strip())

		if type == 1 and encryptions <=10 :

			m = int(input("Give me the plain text now > ").strip())

			r = int(input("Need a random number too > ").strip())

			cipher1 = encrypt(m,r)

			cipher2 = encrypt(m*m,r)


			print("Here are the your encrypted messages : cipher1 = {} and cipher2 = {}\n".format(cipher1,cipher2))


			encryptions +=1


		elif type ==2 :

			r = getRandomRange(1,p-1)

			m = bytes_to_long(flag)

			cipher1 = encrypt(m,r)

			cipher2 = encrypt(m*m,r)

			print("Take this secret message and don't tell anyone : cipher1 = {} and cipher2 = {}\n".format(cipher1,cipher2))


		else:

			print("Ok. Have a nice day. Bye!!\n")
			break

	except:

		print("Something wrong happened. Exiting.\n")
		break
