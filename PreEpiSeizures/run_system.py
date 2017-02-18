from read_system import *
from sync_bitalino import * 

from open_file import *
from close_file import * 
from write_file import *
from read_2_modules import *

import time
import sys

def run_system(device_A, device_B, sync_param, directory):

	print sync_param['strtime']
	

	if time.time()-sync_param['strtime']> 15:
		sync_param['sync_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
		sync_param['dig_Out'] = sync_bitalino(sync_param['dig_Out'], device_A)
		sync_param['flag_sync'] = 1
		sync_param['strtime'] = time.time()


	t = read_2_modules(device_A, device_B)



	if sync_param['flag_sync'] == 1:
		diff = sync_drift(t)
		sync_param['flag_sync'] = 0

	# Open new file each hour
	if time.time()-sync_param['inittime']> 60*60:
		sync_param['close_file'] = 1

	i = time.time() - sync_param['inittime']
	# print elapsed time
	sys.stdout.write("\rElapsed time (seconds): % i " % i)
	sys.stdout.flush()

	write_file(t, diff, a_file, drift_log_file, sync_time)
	#np.savetxt(b_file, b, fmt='%.0f', delimiter='	', newline='\n', header='', footer='', comments ='')

	# Open new file each hour
	if sync_param['close_file'] == 1:
		# close the file
		close_file(a_file, drift_log_file)

		# Open a new file
		a_file, drift_log_file = open_file(directory)

	# -----------------------------------------------------------------
	return sync_param
