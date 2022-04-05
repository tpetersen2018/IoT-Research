import keyboard, socket, time

#server = ("127.0.0.1", 31337)
server = ("0.0.0.0", 31337)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def encrypt(b1, b2=b'\xb7'): # use xor for bytes
    result = bytearray()
    for b1, b2 in zip(b1, b2):
        result.append(b1 ^ b2)
    return bytes(result)

#def encrypt(msg):
#    ciphertext = b'\xb7' ^ msg
#    return ciphertext

print('Use arrow keys to move or press esc to terminate')
while True:
	event = keyboard.read_event()
	if event.event_type == keyboard.KEY_DOWN and event.name == 'esc':
		break
	elif event.event_type == keyboard.KEY_DOWN and event.name == 'up':
		msg = encrypt(b'u')
		sock.sendto(msg, server)
	elif event.event_type == keyboard.KEY_UP and event.name == 'up':
		msg = encrypt(b's')
		sock.sendto(msg, server)
	elif event.event_type == keyboard.KEY_DOWN and event.name == 'down':
		msg = encrypt(b'd')
		sock.sendto(msg, server)
	elif event.event_type == keyboard.KEY_UP and event.name == 'down':
		msg = encrypt(b'stop')
		sock.sendto(msg, server)
	elif event.event_type == keyboard.KEY_DOWN and event.name == 'left':
		msg = encrypt(b'l')
		sock.sendto(msg, server)
	elif event.event_type == keyboard.KEY_UP and event.name == 'left':
		msg = encrypt(b'h')
		sock.sendto(msg, server)
	elif event.event_type == keyboard.KEY_DOWN and event.name == 'right':
		msg = encrypt(b'r')
		sock.sendto(msg, server)
	elif event.event_type == keyboard.KEY_UP and event.name == 'right':
		msg = encrypt(b'halt')
		sock.sendto(msg, server)
	elif event.event_type == keyboard.KEY_DOWN and event.name == 'q':
		msg = encrypt(b'q')
		sock.sendto(msg, server)
		break

time.sleep(1)
