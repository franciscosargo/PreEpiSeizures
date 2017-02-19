from write_drift_log import *
from write_acq_file import *

def write_file(t, diff, a_file, drift_log_file, sync_time):
	write_drift_log(drift_log_file, diff, sync_time)
	write_acq_file(a_file,t)