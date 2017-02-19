from bitalino import *
from connect_system import *
from disconnect_system import *
from create_folder import * 
from start_system import *
from write_file import * 
from run_system import *
from system_except import * 

import sys

#************************************* MAIN SCRIPT*************************************************************

# Use/create the patient folder =============================================================== 
directory = create_folder()

# Prepare the device A ====================================================================

device_A, device_B, a_file, drift_log_file = connect_system(directory)


# Acquisition LOOP =========================================================================
sync_param = start_system(device_A, device_B, a_file, drift_log_file)

#print sync_param['strtime']

print('')
print('The system is running ...'),

	



# Initiate acquisition loop 
while True:

	# try to read from the device--------------------------------------------------------------------------------------------------
	try:
		sync_param = run_system(device_A, device_B, a_file, drift_log_file, sync_param, directory)

	# -------------------------------------------------------------------------------------------------------------------------------

	# Handle misconnection of the devices--------------------------------------------------------------------------------------------
	except Exception as e:
		print ('')
		print ('')
		print ('The system has stopped running because ' + str(e) + '! Please check both Modules!')
		print ('Trying to Reconnect....')

		# Disconnect the system
		disconnect_system(device_A, device_B, a_file, drift_log_file)

		# Reconnect the devices
		device_A, device_B, a_file, drift_log_file = connect_system(directory)

		# Restart the system
		sync_param = start_system(device_A, device_B, a_file, drift_log_file)


		print ('')
		print ('The system is running again ...'),
		
	# -----------------------------------------------------------------------------------------------------------------------------------------

	#Handle user interruption -----------------------------------------------------------------------------------------------------------------
	except KeyboardInterrupt:
		print('')
		print ('You have stopped the acquistion. Saving all the files ...')
		# Disconnect the system
		disconnect_system(device_A, device_B, a_file, drift_log_file)

		break
	# -----------------------------------------------------------------------------------------------------------------------------------------

# =========================================================================================================