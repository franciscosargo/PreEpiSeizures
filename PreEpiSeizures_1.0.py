from bitalino import *
from connect import *
from header2bitalino import*
from syncbitalino import *
from resetsyncbitalino import *
from find_sync import *
from sync_log import *


import time
import os
import sys

# Use/create the patient folder ================================================= 
nb = input('Type in the patients number : ')

directory = "/home/sargo/Desktop/TESE 2017/Acq_PreEpiSeizures/"+str(nb) + "/"
if not os.path.exists(directory):
    os.makedirs(directory)

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


a_file=open(directory + 'A_'+ strftime("%Y-%m-%d %H:%M:%S", gmtime())+'.txt', 'w')
header2bitalino(a_file)

drift_log_file = open(directory + 'drift_log_file_'+ strftime("%Y-%m-%d %H:%M:%S", gmtime())+'.txt', 'w')

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

dig_Out = 0
device_A.trigger([dig_Out,dig_Out]);
device_B.start()
device_A.start()

print('')
print('The system is running ...'),


flag_sync = 0
c=1
inittime = time.time()
strtime = time.time()


# Initiate acquisition loop 
while True:

	# try to read from the device--------------------------------------------------------------------------------------------------
	try:
		# Synchronization 
		if c == 1 or time.time()-strtime> 15:

			# Trigger the digital output
			dig_Out = syncbitalino(dig_Out, device_A)
			
			strtime =  time.time()
			flag_sync = 1
			count_a = 0
			count_b = 0


		a = device_A.read(1000)
		b = device_B.read(1000)

		t = np.concatenate((a, b), axis=1)

		if flag_sync == 1:
			drift, count_a, count_b = sync_drift(t, count_a, count_b)

				



		# update the counter
		c = c+1	

		# update the timer
		i = time.time()-inittime

		# print elapsed time
		sys.stdout.write("\rElapsed time (seconds): % i " % i)
		sys.stdout.flush()

		np.savetxt(a_file, t, fmt='%.0f', delimiter='	', newline='\n', header='', footer='', comments ='')
		#np.savetxt(b_file, b, fmt='%.0f', delimiter='	', newline='\n', header='', footer='', comments ='')

		# Open new file each hour
		if time.time()-inittime> 60*60:
			a_file.close()

			save_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
			
			# Open a new file
			a_file = open(directory + save_time +'.txt', 'w')
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

		# Open a new file
		save_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
		a_file=open(directory + 'A_'+ save_time+'.txt', 'w')
		header2bitalino(a_file)
		drift_log_file = open(directory + 'drift_log_file_'+ save_time, gmtime())+'.txt', 'w')


		# Setting initial digital output settings
		dig_Out = 0
		device_A.trigger([dig_Out,dig_Out]);

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