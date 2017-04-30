import sys
from bitalino import *

def connect(macAddress, init_time):

	if macAddress == "20:16:04:12:01:23":
		mod = 'A'
	else:
		mod = 'B'

	print('Searching for Module '+ str(mod) +' ....')
	
	while True:

		if (time.time() - init_time) > 60:
			sys.exit('Timeout for connection! Exiting python. ')
		try:

			device= BITalino(macAddress)

			# Read BITalino version
			print device.version(),

			print (' Done!')

			return device

		except Exception:
			
			i=1

		




