def start_system(device_A, device_B):

	dig_Out = 0
	device_A.trigger([dig_Out,dig_Out]);
	device_B.start()
	device_A.start()



	return dig_Out