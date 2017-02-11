from bitalino import *
from connect import *
from header2bitalino import*
from syncbitalino import *
from resetsyncbitalino import *

import time
import os
import sys

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

# Prepare the the files for saving data =======================================

#b_file=open('B_'+ strftime("%Y-%m-%d %H:%M:%S", gmtime())+'.txt', 'w')

#a_file.write('# OpenSignals Text File Format'+'\n')
#a_file.write('# {"20:16:04:12:01:40": {"sensor": ["RAW", "RAW", "RAW", "RAW", "RAW", "RAW"], "device name": "A", "column": ["nSeq", "I1", "I2", "O1", "O2", "A1", "A2", "A3", "A4", "A5", "A6"], "sync interval": 2, "time": "19:49:30.350", "comments": "", "device connection": "20:16:04:12:01:40", "channels": [1, 2, 3, 4, 5, 6], "date": "2017-1-31", "mode": 0, "digital IO": [0, 0, 0, 0, 1, 1, 1, 1], "firmware version": "5.1", "device": "bitalino_rev", "position": 0, "sampling rate": 1000, "label": ["A1", "A2", "A3", "A4", "A5", "A6"], "resolution": [4, 1, 1, 1, 1, 10, 10, 10, 10, 6, 6], "special": [{}, {}, {}, {}, {}, {}]}}' +'\n')
#a_file.write('# EndOfHeader'+'\n')


#b_file=open(directory + 'B_'+ strftime("%Y-%m-%d %H:%M:%S", gmtime())+'.txt', 'w')

#b_file.write('# OpenSignals Text File Format'+'\n')
#b_file.write('# {"20:16:04:12:01:40": {"sensor": ["RAW", "RAW", "RAW", "RAW", "RAW", "RAW"], "device name": "B", "column": ["nSeq", "I1", "I2", "O1", "O2", "A1", "A2", "A3", "A4", "A5", "A6"], "sync interval": 2, "time": "19:49:30.350", "comments": "", "device connection": "20:16:04:12:01:40", "channels": [1, 2, 3, 4, 5, 6], "date": "2017-1-31", "mode": 0, "digital IO": [0, 0, 0, 0, 1, 1, 1, 1], "firmware version": "5.1", "device": "bitalino_rev", "position": 0, "sampling rate": 1000, "label": ["A1", "A2", "A3", "A4", "A5", "A6"], "resolution": [4, 1, 1, 1, 1, 10, 10, 10, 10, 6, 6], "special": [{}, {}, {}, {}, {}, {}]}}' +'\n')
#b_file.write('# EndOfHeader'+'\n')

# ==========================================================================================


# Acquisition LOOP =========================================================================

device_A.trigger([0,0]);
device_B.start()
device_A.start()

print('')

print('The system is running ...'),

c=1
inittime = time.time()
strtime = time.time()
# Initiate acquisition loop 
while True:

	# try to read from the device--------------------------------------------------------------------------------------------------
	try:
		a = device_A.read(1000)
		b = device_B.read(1000)

		t = np.concatenate((a, b), axis=1)

		# Initial Synchronization - Time delay deletion
		if c = 1:

			# Get the synchronization output
			a_I1 = t[0:,2]
			b_I1 = t[0:,12]


			sync_value = a_I1[999]

			# Trigger the digital output
			syncbitalino(sync_value, device_A)
			strtime =  time.time()



		# Synchronization 
		if time.time()-strtime> 30:

			# Get the synchronization output
			a_I1 = t[0:,2]
			sync_value = a_I1[999]

			# Trigger the digital output
			syncbitalino(sync_value, device_A)
			strtime =  time.time()

		# update the counter
		c = c+1	

		# update the timer
		i = time.time()-inittime

		sys.stdout.write("\rElapsed time (seconds): % i " % i)
		sys.stdout.flush()


		# Open new file each ~3 minutes
		if time.time()-inittime> 3*60:
			a_file.close()
			
			# Open a new file
			a_file = open(directory + 'A_'+ strftime("%Y-%m-%d %H:%M:%S", gmtime())+'.txt', 'w')
			header2bitalino(a_file)

	# -------------------------------------------------------------------------------------------------------------------------------

	# Handle misconnection of the devices--------------------------------------------------------------------------------------------
	except Exception as e:
		print ('')
		print ('')
		print ('The system has stopped running because ' + str(e) + '! Please check both Modules!')
		print ('Trying to Reconnect....')

		# Close connection from A
		try:
			device_A.stop()
			device_A.close()

		except Exception:
			c=c

		# Close connection from B
		try:
			device_B.stop()
			device_B.close()

		except Exception:
			c=c

		#Close and save files
		a_file.close()
		#b_file.close()

		# Reconnect module A
		device_A = connect(macAddress_A)

		# Reconnect module B
		device_B = connect(macAddress_B)


		# Setting initial digital output settings
		device_A.trigger([0,0]);

		# Restarting the acqusition
		device_A.start(samplingRate_A, acqChannels_A)
		device_B.start(samplingRate_B, acqChannels_B)

		print ('')
		print ('The system is running again ...'),
		
	# -----------------------------------------------------------------------------------------------------------------------------------------


	#Handle user interruption -----------------------------------------------------------------------------------------------------------------
	except KeyboardInterrupt:
		print('')
		print ('You have stopped the acquistion. Saving all the files ...')
		a_file.close()
		#b_file.close()
		break
	# -----------------------------------------------------------------------------------------------------------------------------------------

# =========================================================================================================