from scapy.all import *
import time
from datetime import datetime

CAR1='10.3.142.1'
CAR2='10.3.144.1'
CAR3='10.3.146.1'
CAR4='10.3.147.1'
CAR5='10.3.148.1'

data = {}
data[CAR1]="data/data1.csv"
data[CAR2]="data/data2.csv"
data[CAR3]="data/data3.csv"
data[CAR4]="data/data4.csv"
data[CAR5]="data/data5.csv"

def monitor_pkts(pkt):
 try:
   if pkt.haslayer('UDP'):
      if pkt['UDP'].dport==2022:
         msg="green, %s" %pkt['Raw'].load
         dt = datetime.now()
         ts = datetime.timestamp(dt)
         date_time = datetime.fromtimestamp(ts)
         st = date_time.strftime("%H:%M:%S")
         msg=msg.replace('[Broadcast]',st)
         print(msg)
         CAR = pkt['IP'].src
         f=open(data[CAR],'a')
         f.write(msg+"\n")
         f.close()
 except:
  print("[!] An Error has occured")

def listen():
   conf.iface=="wlan0"
   sniff(filter='ip',prn=monitor_pkts,monitor=True,iface="wlan0")
   #pkts=rdpcap('test.pcap')
   #for pkt in pkts:
   #    monitor_pkts(pkt)

def main():
   listen() 
   pass

if __name__ == '__main__':
   main()
