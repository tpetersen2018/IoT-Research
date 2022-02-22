import wiringpi as GPIO
import socket, select, sys
from signal import *
#import keyboard

# Define pins
ENA = 22
ENB = 30
IN1 = 26
IN3 = 21

# Termination signal handler - makes sure motor is turned off
def clean(*args):
	print('Cleaning up GPIO')
	GPIO.softPwmWrite(ENA, 0)
	GPIO.softPwmWrite(ENB, 0)
	GPIO.digitalWrite(IN1, 0)
	GPIO.digitalWrite(IN3, 0)
	sys.exit(0)

for sig in (SIGABRT, SIGILL, SIGINT, SIGSEGV, SIGTERM, SIGQUIT, SIGTSTP):
	signal(sig, clean)


class WifiCar:
	# Constructor - Need a tuple with 4 GPIO pin numbers: (ENA, ENB, IN1, IN3)
	def __init__(self, ports, freq=100):
		self._epoll = select.epoll()
		self.pwm_freq = freq
		self.ena, self.enb, self.in1, self.in3 = ports
		print(f'IN1:{self.in1}, ENA:{self.ena}')
		print(f'IN3:{self.in3}, ENB:{self.enb}')
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
		# call setup function
		GPIO.wiringPiSetup()
		# Initialize pins as outputs
		GPIO.pinMode(self.ena, GPIO.OUTPUT)
		GPIO.pinMode(self.enb, GPIO.OUTPUT)
		GPIO.pinMode(self.in1, GPIO.OUTPUT)
		GPIO.pinMode(self.in3, GPIO.OUTPUT)
		# Create PWM signals
		GPIO.softPwmCreate(self.ena, 0, 100)
		GPIO.softPwmCreate(self.enb, 0, 100)

	# Turn on PWM
	def turn_on(self, duty=100):
		GPIO.softPwmWrite(self.ena, duty)
		GPIO.softPwmWrite(self.enb, duty)


	# Begin defining directions
	def backward(self):
		
		# Set the gates
		GPIO.digitalWrite(self.in1, GPIO.LOW)
		GPIO.digitalWrite(self.in3, GPIO.HIGH)
		# Set PWM signals
		self.turn_on()

	def forward(self):
		# Set the gates
		GPIO.digitalWrite(self.in1, GPIO.HIGH)
		GPIO.digitalWrite(self.in3, GPIO.LOW)
		# Turn on motor
		self.turn_on()

	def left(self):
		# Set the gates
		GPIO.digitalWrite(self.in1, GPIO.LOW)
		GPIO.digitalWrite(self.in3, GPIO.LOW)
		# Turn on motor
		self.turn_on()

	def right(self):
		# Set the gates
		GPIO.digitalWrite(self.in1, GPIO.HIGH)
		GPIO.digitalWrite(self.in3, GPIO.HIGH)
		# Turn on motor
		self.turn_on()

	def stop(self):
		# Set all inputs to low
		GPIO.softPwmWrite(self.ena, 0)
		GPIO.softPwmWrite(self.enb, 0)


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

# pins are ENA, ENB, IN1, IN3
car = WifiCar((ENA, ENB, IN1, IN3))
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


clean()
