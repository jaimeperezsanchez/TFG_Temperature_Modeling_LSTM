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

	#work 0 - 35 min
	time.sleep(2100)

	#work 1 - 30 min
	work()
	time.sleep(300) 
	kill_work()
	time.sleep(60) 
	work()
	work()
	work()
	time.sleep(300) 
	kill_work() 
	kill_work() 
	kill_work()
	time.sleep(60) 
	work()
	work()
	work()
	work()
	work()
	time.sleep(300) 
	kill_work()
	kill_work() 
	kill_work() 
	kill_work()
	kill_work()
	time.sleep(60) 
	work()
	work()
	work()
	time.sleep(300) 
	kill_work() 
	kill_work() 
	kill_work()
	time.sleep(60) 
	work()
	time.sleep(300) 
	kill_work()
	time.sleep(60)

	#work 2  -  40 min
	work()
	time.sleep(360) 
	kill_work()
	time.sleep(120) 
	work()
	work()
	work()
	time.sleep(360) 
	kill_work() 
	kill_work() 
	kill_work()
	time.sleep(120) 
	work()
	work()
	work()
	work()
	work()
	time.sleep(360) 
	kill_work()
	kill_work() 
	kill_work() 
	kill_work()
	kill_work()
	time.sleep(120) 
	work()
	work()
	work()
	time.sleep(360) 
	kill_work() 
	kill_work() 
	kill_work()
	time.sleep(120) 
	work()
	time.sleep(360) 
	kill_work()
	time.sleep(120) 

	#work 3  -  35 min
	time.sleep(2100)


	#Raspi      R2   R4   R6
	#work 0:    O    O    X
	#work 1:    X    O    O
	#work 2:    X    O    X
	#work 3:    O    O    O

	#CPU to 1.4 GHz 
	to_1400MHz()

	#work 0  -  40 min
	work()
	time.sleep(360) 
	kill_work()
	time.sleep(120) 
	work()
	work()
	work()
	time.sleep(360) 
	kill_work() 
	kill_work() 
	kill_work()
	time.sleep(120) 
	work()
	work()
	work()
	work()
	work()
	time.sleep(360) 
	kill_work()
	kill_work() 
	kill_work() 
	kill_work()
	kill_work()
	time.sleep(120) 
	work()
	work()
	work()
	time.sleep(360) 
	kill_work() 
	kill_work() 
	kill_work()
	time.sleep(120) 
	work()
	time.sleep(360) 
	kill_work()
	time.sleep(120) 

	#work 1  -  30 min
	time.sleep(1800)

	#work 2  -  35 min
	time.sleep(2100)

	#work 3  -  40 min
	work()
	time.sleep(360) 
	kill_work()
	time.sleep(120) 
	work()
	work()
	work()
	time.sleep(360) 
	kill_work() 
	kill_work() 
	kill_work()
	time.sleep(120) 
	work()
	work()
	work()
	work()
	work()
	time.sleep(360) 
	kill_work()
	kill_work() 
	kill_work() 
	kill_work()
	kill_work()
	time.sleep(120) 
	work()
	work()
	work()
	time.sleep(360) 
	kill_work() 
	kill_work() 
	kill_work()
	time.sleep(120) 
	work()
	time.sleep(360) 
	kill_work()
	time.sleep(120) 
