from sync_bitalino import * 
from write_file import * 
import time
from read_2_modules import * 
from sync_drift import * 
from bitalino import *
from system_except import * 
import sys


def start_system(device_A, device_B, a_file, drift_log_file):


	#sync_param = {'flag_sync' : 0 , 'inittime' : time.time(), 'strtime' : time.time(), 'dig_Out' : dig_Out, 'close_file' : 0}

	while True:

		dig_Out = 0
		sync_param = {'flag_sync' : 0 , 'inittime' : time.time(), 'strtime': time.time(), 'sync_time' : time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()), 'dig_Out' : dig_Out, 'close_file' : 0, 'diff': 1000}
		sync_param['dig_Out'] = sync_bitalino(dig_Out,device_A)

		try:

			device_B.start()
			device_A.start()

			# Default to 0
			sync_param['dig_Out'] = sync_bitalino(sync_param['dig_Out'],device_A)
			t = read_2_modules(device_A,device_B)

			sync_param['diff'] = sync_drift(t)
			write_file(t, sync_param['diff'], a_file, drift_log_file, sync_param['sync_time'])
			print('ola')
			break


		except ConnectionBad:

			sys.stdout.write("\rThe system is not prepared")
			sys.stdout.flush()

			device_A.stop()
			device_B.stop()

	
	return sync_param
	