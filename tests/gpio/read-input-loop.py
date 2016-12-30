## EXAMPLE CODE
# Set the GPIO to input, then read and print the value every second

import time
import onionGpio

gpioNum = 7
gpioObj	= onionGpio.OnionGpio(gpioNum)

# set to input 
status 	= gpioObj.setInputDirection()

# read and print the value once a second
loop = 1
while loop == 1:
	value = gpioObj.getValue()
	print 'GPIO%d input value: %d'%(gpioNum, int(value))
	
	time.sleep(1)

