import os
import time

def work():
	os.system('sudo python a.py &')
	os.system('sudo python a.py &')
	os.system('sudo python a.py &')
	os.system('sudo python a.py &')
	os.system('sudo python a.py &')
	os.system('sudo python a.py &')

def kill_work():
	os.system('sudo pkill -n python')
	os.system('sudo pkill -n python')
	os.system('sudo pkill -n python')
	os.system('sudo pkill -n python')
	os.system('sudo pkill -n python')
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

	#work 0
	time.sleep(240) #4 min
	time.sleep(120) #2 min

	#work 1
	work()
	time.sleep(420) #7 min
	kill_work()
	time.sleep(60)  #1 min

	#work 2
	work()
	time.sleep(300) #5 min
	kill_work()
	time.sleep(180) #3 min

	#work 3
	time.sleep(180) #3 min
	time.sleep(120) #2 min


	#Raspi      R2   R4   R6
	#work 0:    O    O    X
	#work 1:    X    O    O
	#work 2:    X    O    X
	#work 3:    O    O    O

	#CPU to 1.4 GHz 
	to_1400MHz()

	#work 0
	work()
	time.sleep(420) #7 min
	kill_work()
	time.sleep(60)  #1 min

	#work 1
	time.sleep(180) #3 min
	time.sleep(120) #2 min

	#work 2
	time.sleep(240) #4 min
	time.sleep(120) #2 min

	#work 3
	work()
	time.sleep(300) #5 min
	kill_work()
	time.sleep(180) #3 min

	
