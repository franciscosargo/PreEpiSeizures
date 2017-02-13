from bitalino import *
from connect_system import *
from disconnect_system import *
from header2bitalino import*
from sync_bitalino import *
from sync_drift import *
from write_drift_log import *
from write_acq_file import *
from create_folder import * 
from open_file import * 

import sys

#************************************* MAIN SCRIPT*************************************************************

# Use/create the patient folder ================================================= 
directory = create_folder()


# Prepare the device A ==========================================================

device_A, device_B = connect_system()

# =============================================================================

# Prepare the the files for saving data =======================================


# Open a new file
a_file, drift_log_file = open_file(directory)

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
			sync_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
			dig_Out = sync_bitalino(dig_Out, device_A)
			strtime =  time.time()
			flag_sync = 1
			count_a = 0
			count_b = 0


		a = device_A.read(1000)
		b = device_B.read(1000)

		t = np.concatenate((a, b), axis=1)

		if flag_sync == 1:
			drift, count_a, count_b = sync_drift(t, count_a, count_b)
			flag_sync = 0
			write_drift_log(drift_log_file, drift, sync_time)

				
		# update the counter
		c = c+1	

		# update the timer
		i = time.time()-inittime

		# print elapsed time
		sys.stdout.write("\rElapsed time (seconds): % i " % i)
		sys.stdout.flush()


		write_acq_file(a_file,t)
		#np.savetxt(b_file, b, fmt='%.0f', delimiter='	', newline='\n', header='', footer='', comments ='')

		# Open new file each hour
		if time.time()-inittime> 60*60:
			# close the file
			a_file.close()

			# Open a new file
			a_file, drift_log_file = open_file(directory)

	# -------------------------------------------------------------------------------------------------------------------------------

	# Handle misconnection of the devices--------------------------------------------------------------------------------------------
	except Exception as e:
		print ('')
		print ('')
		print ('The system has stopped running because ' + str(e) + '! Please check both Modules!')
		print ('Trying to Reconnect....')

		# Disconnect the system
		disconnect_system(device_A, device_B, a_file)

		# Close the file
		a_file.close()

		# Reconnect the devices
		device_A, device_B = connect_system()

		# Open a new file
		a_file, drift_log_file = open_file(directory)

		# Setting initial digital output settings
		dig_Out = 0
		device_A.trigger([dig_Out,dig_Out]);

		# Restarting the acqusition
		device_B.start()
		device_A.start()

		strtime = time.time()
		c = 1
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