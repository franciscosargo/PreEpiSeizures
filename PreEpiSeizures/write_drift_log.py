import numpy as np

def write_drift_log(filename, drift, sync_time):
	filename.write('%i' % drift)
	filename.write('%s' % '  ' + sync_time + '\n')
