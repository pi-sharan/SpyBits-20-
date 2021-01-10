from pwn import *
from binascii import unhexlify


rV = 1581

r = process(['python3','server.py'])

r.sendlineafter("> ",b"1")

m = bytes(1581//8)

r.sendlineafter("> ",m)

keystream = unhexlify(r.recvline().strip().decode().split(": ")[1].encode())

# decrypt flag from 2nd char , starting from 1585th bit, 1st bit of 2nd character == 3rd bit from start (0 indexing)

r.sendlineafter("> ",b"2")

enc = unhexlify(r.recvline().strip().decode().split(": ")[1].encode())

# dont need first 3 bits of `keystream`

out=""

for i in range(len(keystream)):

	block = keystream[i]

	if i==0:

		out += bin(block&(0x1f))[2:].zfill(5)

	else:

		out += bin(block)[2:].zfill(8)



flag="s"

for i in range(len(enc)-1):

	flag += chr( enc[i+1] ^ int( out[ i*8 : (i+1)*8 ] , 2 ) )

	print(flag)
