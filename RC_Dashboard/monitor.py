from scapy.all import *
import time

CAR1='aa:bb:cc:dd:ee:f1'
CAR2='aa:bb:cc:dd:ee:f2'
CAR3='aa:bb:cc:dd:ee:f3'
CAR4='aa:bb:cc:dd:ee:f4'
CAR5='aa:bb:cc:dd:ee:f5'

data = {}
data[CAR1]="data/data1.csv"
data[CAR2]="data/data2.csv"
data[CAR3]="data/data3.csv"
data[CAR4]="data/data4.csv"
data[CAR5]="data/data5.csv"

def monitor_pkts(pkt):
   if pkt.haslayer('UDP'):
      if pkt['UDP'].dport==2022:
         msg="green, %s" %pkt['Raw'].load
         print(msg)
         f=open(data[CAR1],'a')
         f.write(msg+"\n")
         f.close()

def listen():
   conf.iface=="wlan0"
   sniff(filter='ip',prn=monitor_pkts,monitor=True,iface="wlan0")

def main():
   listen() 
   pass

if __name__ == '__main__':
   main()
