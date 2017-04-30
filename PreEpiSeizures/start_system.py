from sync_bitalino import * 
from write_file import * 
import time
from read_2_modules import * 
from sync_drift import * 
from bitalino import *
from system_except import * 
import sys
import numpy as np


def start_system(device_A, device_B, a_file, drift_log_file):


	#sync_param = {'flag_sync' : 0 , 'inittime' : time.time(), 'strtime' : time.time(), 'dig_Out' : dig_Out, 'close_file' : 0}


	dig_Out = 0
	sync_param = {'flag_sync' : 0 , 'inittime' : time.time(), 'strtime': time.time(), 'sync_time' : time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()), 'dig_Out' : dig_Out, 'close_file' : 0, 'diff': 1000, 'save_log': 1, 'count_a': 1000, 'sync_append': 0, 'sync_arr_A': np.zeros(1000, dtype = float), 'sync_arr_B': np.zeros(1000, dtype = float)}
	
	sync_param['dig_Out'] = sync_bitalino(dig_Out,device_A)
	device_B.start()
	device_A.start()

	# Default to 0
	sync_param['dig_Out'] = sync_bitalino(sync_param['dig_Out'],device_A)
	t,t_str = read_2_modules(device_A,device_B)

	#sync_param['diff'], sync_param['count_a'] = sync_drift(t)
	sync_param['save_log'] = 1
			
	write_file(t, a_file, drift_log_file, sync_param, str(sync_param['inittime']))
	print 'done'                    

			
			
		
	
	return sync_param
	
