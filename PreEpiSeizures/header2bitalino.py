

def header2bitalino(filename, file_time, file_date): 
	filename.write('# OpenSignals Text File Format'+'\n')
	filename.write('# {"20:16:04:12:01:23": {"sensor": ["RAW", "RAW", "RAW", "RAW", "RAW", "RAW"], "device name": "Device 1", "column": ["nSeq", "I1", "I2", "O1", "O2", "A1", "A2", "A3", "A4", "A5", "A6"], "sync interval": 2, "time": ' + file_time+', "comments": "", "device connection": "20:16:04:12:01:40", "channels": [1, 2, 3, 4, 5, 6], "date": '+file_date+', "mode": 0, "digital IO": [0, 0, 0, 0, 1, 1, 1, 1], "firmware version": "5.1", "device": "bitalino_rev", "position": 0, "sampling rate": 1000, "label": ["EDA", "BVP", "EMG", "Acc X", "Acc Y", "Acc Z"], "resolution": [4, 1, 1, 1, 1, 10, 10, 10, 10, 6, 6], "special": [{}, {}, {}, {}, {}, {}]}, "20:16:04:12:01:40": {"sensor": ["RAW", "RAW", "RAW", "RAW", "RAW", "RAW"], "device name": "Device 2", "column": ["nSeq", "I1", "I2", "O1", "O2", "A1", "A2", "A3", "A4", "A5", "A6"], "sync interval": 2, "time": ' + file_time + ', "comments": "", "device connection": "20:16:04:12:01:23", "channels": [1, 2, 3, 4, 5, 6], "date": ' + file_date + ', "mode": 0, "digital IO": [0, 0, 0, 0, 1, 1, 1, 1], "firmware version": "5.1", "device": "bitalino_rev", "position": 1, "sampling rate": 1000, "label": ["EOG", "ECG", "PZT", "Acc X", "Acc Y", "Acc Z"], "resolution": [4, 1, 1, 1, 1, 10, 10, 10, 10, 6, 6], "special": [{}, {}, {}, {}, {}, {}]}}' +'\n')
	filename.write('# EndOfHeader'+'\n')





