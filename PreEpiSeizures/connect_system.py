from connect import *
from open_file import *


def connect_system(directory):
	# Prepare the device A ==========================================================

	macAddress_A= "20:16:04:12:01:23"
	batteryThreshold_A = 30
	acqChannels_A = [0,1,2,3,4,5]
	samplingRate_A = 1000
	nSamples_A = 5
	digitalOutput_A= [0,0]

	# Connect to BITalino
	init_connect_A_time = time.time() 
	device_A = connect(macAddress_A,init_connect_A_time)

	# ==============================================================================

	# Prepare the device B =========================================================

	macAddress_B = "20:16:04:12:01:40"
	batteryThreshold_B = 30
	acqChannels_B = [0,1,2,3,4,5]
	samplingRate_B = 1000
	nSamples_B = 5
	digitalOutput_B = [0,0]

	# Connect to BITalino
	init_connect_B_time = time.time()
	device_B = connect(macAddress_B,init_connect_B_time)

	# =============================================================================

	a_file, drift_log_file = open_file(directory)


	return device_A, device_B, a_file, drift_log_file