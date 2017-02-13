import time

def sync_bitalino(value,device):
	#print ('')
	#print ('Sychronizing...'),

	sync_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())

	if value == 0:
		value = 1
		device.trigger([1,1]);

		#print (str(value))
	else:
		value = 0
		device.trigger([0,0]);
		#print (str(value))

	print ('Done!')

			
	return value, sync_time
