import sys
from bitalino import *

def connect(macAddress):

	if macAddress == "20:16:04:12:01:23":
		mod = 'A'
	else:
		mod = 'B'

	print('Searching for Module'+ str(mod) +' ....')
	
	while True:

		try:

			device= BITalino(macAddress)

			# Read BITalino version
			print device.version(),

			print (' Done!')

			return device

		except Exception:
			
			i=1

		




