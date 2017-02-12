def sync_bitalino(value,device):
	print ('')
	print ('Sychronizing...'),

	if value == 0:
		value = 1
		device.trigger([1,1]);

		print (str(value))
	else:
		value = 0
		device.trigger([0,0]);
		print (str(value))

	print ('Done!')
	return value