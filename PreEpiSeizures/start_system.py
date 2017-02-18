from sync_bitalino import * 
from write_file import * 
import time

def start_system(device_A, device_B, a_file, drift_log_file):

	dig_Out = 0
	digOut = sync_bitalino(dig_Out, device_A);
	device_B.start()
	device_A.start()

	sync_param = {'flag_sync' : 0 , 'inittime' : time.time(), 'strtime' : time.time(), 'dig_Out' : dig_Out, 'close_file' : 0}

	while True:

		try:

			# Default to 0
			sync_param['dig_Out'] = sync_bitalino(digOut,device_A)

			t = read_2_modules(device_A,device_B)

			diff = sync_drift(t)

			write_file(t, diff, a_file, drift_log_file, sync_time)


		except Exception("the Connection between the Modules has been severed"):
			print ('The System is not properly prepared') 

		except Exception:
			break


	return sync_param