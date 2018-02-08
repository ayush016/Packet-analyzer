import sys
import os
import time
import matplotlib.pyplot as plt
import numpy as np
from time import sleep
z=os.system("clear")
print "\t\t\tWelcome to Packets exchange analysis\n\n"
interface = raw_input("Enter Name of your Network Interface you want to capture packet?\n")
print '''1. Capture Packets by Port 
2. Capture packets by Destination host 
3. Capture Packets by Sorce host
4. Capture packets by Destination host and port
5. Capture packets by Source host and port
6. Default Capturing
7. Output Packets (Source and Destination Host only)
'''
option = raw_input()
option=int(option)
#port = raw_input("\nEnter Port Number : ")

if(option==1):
	port = raw_input("\nEnter Port Number : ")
elif(option==2):
	host = raw_input("\nEnter Destination Host IP : ")
elif(option==3):
	src = raw_input("\nEnter Source Host IP : ")
elif(option==4):
	src = raw_input("\nEnter Destination Host IP : ")
	port = raw_input("\nEnter Port Number : ")
elif(option==5):
	src = raw_input("\nEnter Source Host IP : ")
	port = raw_input("\nEnter Port Number : ")
elif(option==7):
	port = raw_input("\nEnter Port Number (Enter -1 if you dont want to specify port) : ")



pid = os.fork()

if(pid==0):
    	if(option==1):
		os.system("sudo tcpdump -i "+interface+" port "+port+" -n > test.txt")
	elif(option==2):
		os.system("sudo tcpdump -i "+interface+" dst host "+host+" -n > test.txt")
	elif(option==3):
		os.system("sudo tcpdump -i "+interface+" src host "+host+" -n > test.txt")
	elif(option==4):
		os.system("sudo tcpdump -i "+interface+" dst host "+host+" port "+port+" -n > test.txt")
	elif(option==5):
		os.system("sudo tcpdump -i "+interface+" src host "+host+" port "+port+" -n > test.txt")
	elif(option==6): 
		os.system("sudo tcpdump -i "+interface+" -n > test.txt")
	elif(option==7):
		newport=port 
		newport=int(newport)
		
		if(newport==-1):
			os.system("sudo tcpdump -i "+interface+" -n |grep -o 'IP .*' |cut -d ':' -f 1")
		else:
			os.system("sudo tcpdump -i "+interface+" port "+port+" -n |grep -o 'IP .*' |cut -d ':' -f 1")
		#print "Source \t|\tDestination"
else:
	while(option==7):
		lock=1
	num_lines=0
	j=[]
	i=[]
	p=raw_input("Till how much time(in sec) you want to capture?\n\n ")
	p=(int)(p)
	e=int(time.time())
	k=0
	num_lines=0
	sleep(2)
	while(1>0):
		y=int(time.time())
		sleep(1)
		x=int(sum(1 for line in open('test.txt')))
		if((x-num_lines)>0):
			y=int(time.time())
			print x-num_lines,y-e
			j.append(x-num_lines)
			i.append(y-e)
			k=k+1
			
			plt.scatter(i, j)
			plt.plot(i, j)
			plt.xlabel('Time (in sec)')
			plt.ylabel('Packets Captured (Relative)')
			plt.title('Packets transfer analysis')
                        plt.pause(0.05)
		#print "before",x
		sleep(1)
		num_lines = int(sum(1 for line in open('test.txt')))
		#print "after",num_lines	
		if((num_lines - x)>0):
			y=int(time.time())
			print num_lines - x,y-e
			j.append(num_lines - x)
			i.append(y-e)
			k=k+1
			
			plt.scatter(i, j)
			plt.plot(i, j)
			plt.xlabel('Time (in sec)')
			plt.ylabel('Packets Captured (Relative)')
			plt.title('Packets transfer analysis')
                        plt.pause(0.05)
			#p=p-1
		if(y-e>p):
			break	

	os.system("rm -f test.txt")
	plt.grid(True)
	plt.show()import sys
import os
import time
import matplotlib.pyplot as plt
import numpy as np
from time import sleep
z=os.system("clear")
print "\t\t\tWelcome to Packets exchange analysis\n\n"
interface = raw_input("Enter Name of your Network Interface you want to capture packet?\n")
print '''1. Capture Packets by Port 
2. Capture packets by Destination host 
3. Capture Packets by Sorce host
4. Capture packets by Destination host and port
5. Capture packets by Source host and port
6. Default Capturing
7. Output Packets (Source and Destination Host only)
'''
option = raw_input()
option=int(option)
#port = raw_input("\nEnter Port Number : ")

if(option==1):
	port = raw_input("\nEnter Port Number : ")
elif(option==2):
	host = raw_input("\nEnter Destination Host IP : ")
elif(option==3):
	src = raw_input("\nEnter Source Host IP : ")
elif(option==4):
	src = raw_input("\nEnter Destination Host IP : ")
	port = raw_input("\nEnter Port Number : ")
elif(option==5):
	src = raw_input("\nEnter Source Host IP : ")
	port = raw_input("\nEnter Port Number : ")
elif(option==7):
	port = raw_input("\nEnter Port Number (Enter -1 if you dont want to specify port) : ")



pid = os.fork()

if(pid==0):
    	if(option==1):
		os.system("sudo tcpdump -i "+interface+" port "+port+" -n > test.txt")
	elif(option==2):
		os.system("sudo tcpdump -i "+interface+" dst host "+host+" -n > test.txt")
	elif(option==3):
		os.system("sudo tcpdump -i "+interface+" src host "+host+" -n > test.txt")
	elif(option==4):
		os.system("sudo tcpdump -i "+interface+" dst host "+host+" port "+port+" -n > test.txt")
	elif(option==5):
		os.system("sudo tcpdump -i "+interface+" src host "+host+" port "+port+" -n > test.txt")
	elif(option==6): 
		os.system("sudo tcpdump -i "+interface+" -n > test.txt")
	elif(option==7):
		newport=port 
		newport=int(newport)
		
		if(newport==-1):
			os.system("sudo tcpdump -i "+interface+" -n |grep -o 'IP .*' |cut -d ':' -f 1")
		else:
			os.system("sudo tcpdump -i "+interface+" port "+port+" -n |grep -o 'IP .*' |cut -d ':' -f 1")
		#print "Source \t|\tDestination"
else:
	while(option==7):
		lock=1
	num_lines=0
	j=[]
	i=[]
	p=raw_input("Till how much time(in sec) you want to capture?\n\n ")
	p=(int)(p)
	e=int(time.time())
	k=0
	num_lines=0
	sleep(2)
	while(1>0):
		y=int(time.time())
		sleep(1)
		x=int(sum(1 for line in open('test.txt')))
		if((x-num_lines)>0):
			y=int(time.time())
			print x-num_lines,y-e
			j.append(x-num_lines)
			i.append(y-e)
			k=k+1
			
			plt.scatter(i, j)
			plt.plot(i, j)
			plt.xlabel('Time (in sec)')
			plt.ylabel('Packets Captured (Relative)')
			plt.title('Packets transfer analysis')
                        plt.pause(0.05)
		#print "before",x
		sleep(1)
		num_lines = int(sum(1 for line in open('test.txt')))
		#print "after",num_lines	
		if((num_lines - x)>0):
			y=int(time.time())
			print num_lines - x,y-e
			j.append(num_lines - x)
			i.append(y-e)
			k=k+1
			
			plt.scatter(i, j)
			plt.plot(i, j)
			plt.xlabel('Time (in sec)')
			plt.ylabel('Packets Captured (Relative)')
			plt.title('Packets transfer analysis')
                        plt.pause(0.05)
			#p=p-1
		if(y-e>p):
			break	

	os.system("rm -f test.txt")
	plt.grid(True)
	plt.show()
