import time
from header2bitalino import *  

def open_file(directory):

	# for txt format
	save_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
	a_file=open(directory + 'A_'+ save_time+'.txt', 'w')
	header2bitalino(a_file)
	drift_log_file = open(directory + 'drift_log_file_'+ save_time +'.txt', 'w')

	#b_file=open('B_'+ strftime("%Y-%m-%d %H:%M:%S", gmtime())+'.txt', 'w')

	#a_file.write('# OpenSignals Text File Format'+'\n')
	#a_file.write('# {"20:16:04:12:01:40": {"sensor": ["RAW", "RAW", "RAW", "RAW", "RAW", "RAW"], "device name": "A", "column": ["nSeq", "I1", "I2", "O1", "O2", "A1", "A2", "A3", "A4", "A5", "A6"], "sync interval": 2, "time": "19:49:30.350", "comments": "", "device connection": "20:16:04:12:01:40", "channels": [1, 2, 3, 4, 5, 6], "date": "2017-1-31", "mode": 0, "digital IO": [0, 0, 0, 0, 1, 1, 1, 1], "firmware version": "5.1", "device": "bitalino_rev", "position": 0, "sampling rate": 1000, "label": ["A1", "A2", "A3", "A4", "A5", "A6"], "resolution": [4, 1, 1, 1, 1, 10, 10, 10, 10, 6, 6], "special": [{}, {}, {}, {}, {}, {}]}}' +'\n')
	#a_file.write('# EndOfHeader'+'\n')


	#b_file=open(directory + 'B_'+ strftime("%Y-%m-%d %H:%M:%S", gmtime())+'.txt', 'w')

	#b_file.write('# OpenSignals Text File Format'+'\n')
	#b_file.write('# {"20:16:04:12:01:40": {"sensor": ["RAW", "RAW", "RAW", "RAW", "RAW", "RAW"], "device name": "B", "column": ["nSeq", "I1", "I2", "O1", "O2", "A1", "A2", "A3", "A4", "A5", "A6"], "sync interval": 2, "time": "19:49:30.350", "comments": "", "device connection": "20:16:04:12:01:40", "channels": [1, 2, 3, 4, 5, 6], "date": "2017-1-31", "mode": 0, "digital IO": [0, 0, 0, 0, 1, 1, 1, 1], "firmware version": "5.1", "device": "bitalino_rev", "position": 0, "sampling rate": 1000, "label": ["A1", "A2", "A3", "A4", "A5", "A6"], "resolution": [4, 1, 1, 1, 1, 10, 10, 10, 10, 6, 6], "special": [{}, {}, {}, {}, {}, {}]}}' +'\n')
	#b_file.write('# EndOfHeader'+'\n')

	return a_file, drift_log_file