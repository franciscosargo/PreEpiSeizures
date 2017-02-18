from sync_bitalino import *
import time

def check_sync_system(device_A,device_B, digOut):

while True:
	try:
		{'flag_sync' = 0 , 'inittime' = time.time(), 

		# Default to 0
		digOut, sync_time = sync_bitalino(digOut,device_A)

		t = read_2_modules(device_A,device_B)

		diff = sync_drift(t)

		break

	except Exception("the Connection between the Modules has been severed")
		print ('The System is not properly prepared') 

	except Exception
		break


return t, diff
	



