from connect import *

def connect_system():
	# Prepare the device A ==========================================================

	macAddress_A= "20:16:04:12:01:23"
	batteryThreshold_A = 30
	acqChannels_A = [0,1,2,3,4,5]
	samplingRate_A = 1000
	nSamples_A = 5
	digitalOutput_A= [0,0]

	# Connect to BITalino
	device_A = connect(macAddress_A)

	# ==============================================================================

	# Prepare the device B =========================================================

	macAddress_B = "20:16:04:12:01:40"
	batteryThreshold_B = 30
	acqChannels_B = [0,1,2,3,4,5]
	samplingRate_B = 1000
	nSamples_B = 5
	digitalOutput_B = [0,0]

	# Connect to BITalino
	device_B = connect(macAddress_B)

	# =============================================================================



	return device_A, device_B