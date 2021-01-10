from pwn import *
from Crypto.Util.number import *

#r=process(["python3","server.py"])

r=remote("52.205.18.68",5001)

r.recvuntil(": ")

ciphertext=int(r.recvline().strip(),16)

def getoutput(type,val):

	r.sendlineafter("> ",str(type))
	r.sendlineafter("> ",str(val))
	r.recvuntil("message : ")
	return int(r.recvline().strip(),16)

c00 = getoutput(1,2)
c01 = getoutput(1,4)
v1 = c00*c00-c01

c10 = getoutput(1,3)
c11 = getoutput(1,9)
v2 = c10*c10-c11

N = GCD(v1,v2)

c2=(pow(2,0x10001,N)*ciphertext)%N

m2=getoutput(2,c2)

print(long_to_bytes(m2//2))
