import socket
import fcntl
import struct
import os
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915, 
        struct.pack('256s', ifname[:15])
    )[20:24])

x=os.system("ip link|grep 'state UP'|cut -d ':' -f 2 > NetworkInterface.txt")
#print x
f=open("NetworkInterface.txt","r")
line = f.readlines()
k=[]
count=0
for i in line:
	k.append(i)
	k[count]=k[count].replace('\n','')
	k[count]=k[count].replace(' ','')
	count = count +1
g = open("NetworkInterface.txt","w")
count_new = 0
for i in line:
	g.write(k[count_new])
	count_new = count_new + 1
g.close()
#print k[0]
print get_ip_address(k[0])

