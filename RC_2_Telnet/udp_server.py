import RPi.GPIO as GPIO
import socket, select, sys
import keyboard

GPIO.cleanup()

class WifiCar:
	# Constructor - Need a tuple with 6 GPIO pin numbers: (IN1, IN2, IN3, IN4, ENA, ENB)
	def __init__(self, ports, freq=100):
		self._epoll = select.epoll()
		self.pwm_freq = freq
		self.in1, self.in2, self.ena, self.in3, self.in4, self.enb = ports
		print(f'IN1:{self.in1}, IN2:{self.in2}, ENA:{self.ena}')
		print(f'IN3:{self.in3}, IN4:{self.in4}, ENB:{self.enb}')
		self.client_socks = {}

	def initialize_udpserver(self, port=31337):
		self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		#self.serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.serversocket.bind(('0.0.0.0', port))
		#self.serversocket.listen(1)
		#self.serversocket.setblocking(0)
		# Register the socket
		self._epoll.register(self.serversocket, select.EPOLLIN)


	def initialize_gpio(self, duty=50):
		GPIO.setmode(GPIO.BOARD)	# use board pin numbers
		gates = (self.in1, self.in2, self.in3, self.in4)
		# Initialize the IN gates to be output low
		GPIO.setup(gates, GPIO.OUT)
		GPIO.output(gates, GPIO.LOW)
		# Setup the PWM signals
		GPIO.setup((self.ena, self.enb), GPIO.OUT)
		self.pwm_l = GPIO.PWM(self.ena, self.pwm_freq)
		self.pwm_r = GPIO.PWM(self.enb, self.pwm_freq)
		self.duty = duty
		self.pwm_l.start(duty)
		self.pwm_r.start(duty)

	# Begin defining directions
	def backward(self):
		# Set IN2 & IN4 low FIRST
		GPIO.output((self.in2, self.in4), GPIO.LOW)
		# Now set IN1 & IN3 high
		GPIO.output((self.in1, self.in3), GPIO.HIGH)

	def forward(self):
		# Set IN1 & IN3 low
		GPIO.output((self.in1, self.in3), GPIO.LOW)
		# Now set IN2 & IN4 high
		GPIO.output((self.in2, self.in4), GPIO.HIGH)

	def left(self):
		# Set IN1 & IN4 low first
		GPIO.output((self.in1, self.in4), GPIO.LOW)
		# Now set IN2 & IN3 high
		GPIO.output((self.in2, self.in3), GPIO.HIGH)

	def right(self):
		# SET IN2 & IN3 low first
		GPIO.output((self.in2, self.in3), GPIO.LOW)
		# Now set IN1 & IN4 high
		GPIO.output((self.in1, self.in4), GPIO.HIGH)

	def stop(self):
		# Set all inputs to low
		GPIO.output((self.in1, self.in2, self.in3, self.in4), GPIO.LOW)


	def runserver(self, callback, timeout=1):
		events = self._epoll.poll(timeout)
		for fileno, event in events:

			# receiving input from client
			if event & select.EPOLLIN:
				content, addr = self.serversocket.recvfrom(1024, socket.MSG_DONTWAIT)
				if not content or not content.strip():
					break
				else:
					callback(self.serversocket, addr, content.strip())




pins = (11, 12, 13, 15, 16, 18)
car = WifiCar(pins)
FLAG = True

# define our socket callback
def udp_socket_callback(sock, client, msg):
	print(f"Received command {msg} from {client}")
	if msg == b'u':
		car.forward()
		sock.sendto(b'Going forwards\n', client)
	elif msg == b'd':
		sock.sendto(b"Going backwards\n", client)
		car.backward()
	elif msg == b'l':
		sock.sendto(b"Turning left\n", client)
		car.left()
	elif msg == b'r':
		sock.sendto(b"Turning right\n", client)
		car.right()
	else:
		car.stop()
		if msg == b'q':
			sock.sendto(b'Shutting down\n', client)
			global FLAG
			FLAG = False
		else:
			sock.sendto(b'Platform stopped\n', client)

#sys.exit()
car.initialize_gpio()
car.initialize_udpserver()
car.runserver(udp_socket_callback)


# Keyboard testing
print('Use arrow keys to move or press esc to terminate')
while FLAG:
	car.runserver(udp_socket_callback)


GPIO.cleanup()





















