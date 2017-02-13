import numpy as np

def write_acq_file(a_file, t):
	np.savetxt(a_file, t, fmt='%.0f', delimiter='	', newline='\n', header='', footer='', comments ='')