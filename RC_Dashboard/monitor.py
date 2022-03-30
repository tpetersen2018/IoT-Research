CAR1=aa:bb:cc:dd:ee:f1
CAR2=aa:bb:cc:dd:ee:f2
CAR3=aa:bb:cc:dd:ee:f3
CAR4=aa:bb:cc:dd:ee:f4
CAR5=aa:bb:cc:dd:ee:f5

data = {}
data[CAR1]="data/data1.csv"
data[CAR2]="data/data2.csv"
data[CAR3]="data/data3.csv"
data[CAR4]="data/data4.csv"
data[CAR5]="data/data5.csv"

from scapy.all import *

def write_broadcast(pkt):
    print("[+] Broadcast Detected")

def write_new_wifi_connection(pkt):
    print("[+] New WiFi Connection")

def write_new_udp_connection(pkt):
    print("[+] New UDP Connection")

'''
monitor 
--> detect broadcast: (udp/255.255.255.255)
--> detect wifi connection (802.11/sta)
--> detect udp connect: (udp/correct port)
--> what else?
'''
