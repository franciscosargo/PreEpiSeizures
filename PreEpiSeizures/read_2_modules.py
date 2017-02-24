import numpy as np

def read_2_modules(device_A, device_B):

	a = device_A.read(1000)
	b = device_B.read(1000)

	t = np.concatenate((a, b), axis=1)

	return t