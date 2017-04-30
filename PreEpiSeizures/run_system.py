
from sync_bitalino import * 
from sync_drift import*
from open_file import *
from close_file import * 
from write_file import *
from read_2_modules import *
from datetime import datetime, timedelta

import time
import sys
import socket


def run_system(device_A, device_B, a_file, drift_log_file, sync_param, directory):
	

	if time.time()-sync_param['strtime'] > 5:
		sync_param['dig_Out'] = sync_bitalino(sync_param['dig_Out'], device_A)
		sync_param['strtime'] = time.time()
		now = datetime.now()
		sync_time = now.strftime("%Y-%m-%d %H:%M:%S.%f").rstrip('0')
		sync_param['sync_time'] = sync_time
		sync_param['connection'] = 1
		sync_param['sync_append'] = 0
		sync_param['sync_arr_A'] = np.zeros(1000, dtype = float)
		sync_param['sync_arr_B'] = np.zeros(1000, dtype = float)

	t, t_str = read_2_modules(device_A, device_B)
	MESSAGE = t_str
	UDP_IP = "127.0.0.1"
	UDP_PORT = 5005

	#print 
	#print len(t_str)
	try:
		sock = socket.socket(socket.AF_INET, # Internet
	                     	socket.SOCK_DGRAM) # UDP
		sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
	except Exception as e:
		print e
		pass

	if sync_param['sync_append'] > -1:
		c = sync_param['sync_append'] 
		sync_param['sync_arr_A'][((c*100)):((c+1)*100)] =  t[0:,4]
		sync_param['sync_arr_B'][((c*100)):((c+1)*100)] =  t[0:,12]
		sync_param['sync_append'] += 1


	if  sync_param['sync_append'] == 10:
		sync_param['diff'], sync_param['count_a'] = sync_drift(sync_param['sync_arr_A'], sync_param['sync_arr_B'])
		#print sync_param['diff']
		sync_param['save_log'] = 1
		sync_param['sync_append'] = -1

	# Open new file each hour
	if time.time()-sync_param['inittime']> 60*60:
		sync_param['close_file'] = 1

	i = time.time() - sync_param['inittime']

	# print elapsed time
	sys.stdout.write("\rElapsed time (seconds): % i " % i)
	sys.stdout.flush()

	write_file(t, a_file, drift_log_file, sync_param, str(i))

	# Open new file each hour
	if sync_param['close_file'] == 1:
		# close the file
		print('closing')
		close_file(a_file, drift_log_file)

		# Open a new file
		print('Opening new file')
		a_file, drift_log_file = open_file(directory)

		sync_param['close_file'] = 0
		sync_param['inittime'] = time.time()

	# -----------------------------------------------------------------
	return a_file, drift_log_file, sync_param
