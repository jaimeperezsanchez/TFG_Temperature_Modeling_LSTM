import os
import time

def work():
	os.system('sudo python a.py &')

def kill_work():
	os.system('sudo pkill -n python')

def to_600MHz():
	os.system('sudo cpufreq-set -r -g userspace')
	os.system('sudo cpufreq-set -r -f 600MHz')

def to_1400MHz():
	os.system('sudo cpufreq-set -r -g userspace')
	os.system('sudo cpufreq-set -r -f 1.4GHz')


while(True):
	#Raspi      R2   R4   R6
	#work 0:    X    O    X
	#work 1:    O    O    X
	#work 2:    O    O    O
	#work 3:    X    O    O

	#CPU to 600 MHz
	to_600MHz()

	#work 0  -  23 min
	work()
	time.sleep(180) 
	work()
	time.sleep(120) 
	work()
	time.sleep(260) 
	work()
	time.sleep(180) 
	work()
	time.sleep(300) 
	kill_work()
	time.sleep(60)  
	kill_work()
	time.sleep(100)  
	kill_work()
	time.sleep(80) 
	kill_work()
	time.sleep(50) 
	kill_work()
	time.sleep(50)  

	#work 1  -  15 min
	work()
	time.sleep(90) 
	work()
	time.sleep(140) 
	work()
	time.sleep(110) 
	work()
	time.sleep(80) 
	work()
	time.sleep(250) 
	kill_work()
	time.sleep(40)  
	kill_work()
	time.sleep(20)  
	kill_work()
	time.sleep(80) 
	kill_work()
	time.sleep(40) 
	kill_work()
	time.sleep(50) 

	#work 2  -  19 min
	work()
	time.sleep(120) 
	work()
	time.sleep(90) 
	work()
	time.sleep(200) 
	work()
	time.sleep(160) 
	work()
	time.sleep(300) 
	kill_work()
	time.sleep(60)  
	kill_work()
	time.sleep(50)  
	kill_work()
	time.sleep(80) 
	kill_work()
	time.sleep(30) 
	kill_work()
	time.sleep(50)  

	#work 3  -  22 min
	work()
	time.sleep(120) 
	work()
	time.sleep(100) 
	work()
	time.sleep(240) 
	work()
	time.sleep(180) 
	work()
	time.sleep(320) 
	kill_work()
	time.sleep(90)  
	kill_work()
	time.sleep(100)  
	kill_work()
	time.sleep(70) 
	kill_work()
	time.sleep(40) 
	kill_work()
	time.sleep(60)  


	#Raspi      R2   R4   R6
	#work 0:    O    O    X
	#work 1:    X    O    O
	#work 2:    X    O    X
	#work 3:    O    O    O

	#CPU to 1.4 GHz 
	to_1400MHz()

	#work 0  -  15 min
	work()
	time.sleep(90) 
	work()
	time.sleep(140) 
	work()
	time.sleep(110) 
	work()
	time.sleep(80) 
	work()
	time.sleep(250) 
	kill_work()
	time.sleep(40)  
	kill_work()
	time.sleep(20)  
	kill_work()
	time.sleep(80) 
	kill_work()
	time.sleep(40) 
	kill_work()
	time.sleep(50) 

	#work 1  -  22 min
	work()
	time.sleep(120) 
	work()
	time.sleep(100) 
	work()
	time.sleep(240) 
	work()
	time.sleep(180) 
	work()
	time.sleep(320) 
	kill_work()
	time.sleep(90)  
	kill_work()
	time.sleep(100)  
	kill_work()
	time.sleep(70) 
	kill_work()
	time.sleep(40) 
	kill_work()
	time.sleep(60) 

	#work 2  -  19 min
	work()
	time.sleep(120) 
	work()
	time.sleep(90) 
	work()
	time.sleep(200) 
	work()
	time.sleep(160) 
	work()
	time.sleep(300) 
	kill_work()
	time.sleep(60)  
	kill_work()
	time.sleep(50)  
	kill_work()
	time.sleep(80) 
	kill_work()
	time.sleep(30) 
	kill_work()
	time.sleep(50) 

	#work 3  -  23 min
	work()
	time.sleep(180) 
	work()
	time.sleep(120) 
	work()
	time.sleep(260) 
	work()
	time.sleep(180) 
	work()
	time.sleep(300) 
	kill_work()
	time.sleep(60)  
	kill_work()
	time.sleep(100)  
	kill_work()
	time.sleep(80) 
	kill_work()
	time.sleep(50) 
	kill_work()
	time.sleep(50)  

	
