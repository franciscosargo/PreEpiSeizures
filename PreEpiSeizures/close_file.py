from close_acq_file import *
from close_drift_log_file import *

def close_file(a_file, log_drift_file):
        print('closing')
	close_acq_file(a_file)
	close_drift_log_file(log_drift_file)

