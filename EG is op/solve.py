from pwn import *
from Crypto.Util.number import *
from gmpy2 import next_prime


io = process(['python3','server.py'])

def getEnc(r):

	io.sendlineafter("> ",b"1")
	io.sendlineafter("> ",b"1")
	io.sendlineafter("> ",r)
	return int(io.recvline().strip().decode().split("(")[1].split(",")[0])


g = getEnc(b"1")

g2 = getEnc(b"2")

g3 = getEnc(b"3")

g4 = getEnc(b"4")

p = GCD( g*g - g2 , g*g*g -g3 )

p = GCD( p , g*g*g*g -g4 )

i=2
while i<1000:

	while p%next_prime(i)==0: p%=next_prime(i)
	i = next_prime(i)

assert isPrime(p)

io.sendlineafter("> ",b"2")

data = io.recvline().strip().decode().split(", ")


cipher1 = int(data[1].split(")")[0])
cipher2 = int(data[2].split(")")[0])

flag = inverse(cipher1,p) * cipher2 % p

print(long_to_bytes(flag))

