from close_file import * 
from bitalino import * 
def disconnect_system(device_A, device_B, a_file, drift_log_file): 

	# Close connection from A
	try:
		device_A.stop()
		device_A.close()

	except Exception:
		pass

	# Close connection from B
	try:
		device_B.stop()
		device_B.close()
                      
	except Exception:
		pass

	close_file(a_file, drift_log_file)
