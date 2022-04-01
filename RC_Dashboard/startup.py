import os

def start_up():
   os.system('ifconfig wlan0 down')
   os.system('iwconfig wlan0 mode monitor')
   os.system('ifconfig wlan0 up')
   os.system('iwconfig wlan0 channel 11')

def main():
   start_up()

if __name__ == '__main__':
   main()
