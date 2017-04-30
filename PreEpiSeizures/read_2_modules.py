import numpy as np
import pickle

def read_2_modules(device_A, device_B):

	a = device_A.read(100)
	b = device_B.read(100)

	t = np.concatenate((a, b), axis=1)
	t_str = '\n'.join(' '.join('%0.1f' %x for x in y) for y in t)


	return t, t_str