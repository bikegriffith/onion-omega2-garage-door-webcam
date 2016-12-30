## EXAMPLE CODE
# Set the GPIO to output, read and print the initial value

import onionGpio

gpioNum = 6
gpioObj	= onionGpio.OnionGpio(gpioNum)

# set to input 
status 	= gpioObj.setOutputDirection()
print 'GPIO%d set to output,'%(gpioNum),

# read the value
value 	= gpioObj.getValue()
print ' initial value: %d'%(int(value))


## GOING FURTHER
# Try changing line 10 to: 
#  status 	= gpioObj.setOutputDirection(0)
# or
#  status 	= gpioObj.setOutputDirection(1)
#
# And see how the initial value changes :)
#
