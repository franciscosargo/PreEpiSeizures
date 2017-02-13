
from find_sync import *

def sync_drift(t):
	a_I1 = t[0:,2]
	b_I1 = t[0:,12]
	count_a_t = find_sync(a_I1)
	count_b_t = find_sync(b_I1)

	print count_a_t
	print count_b_t

	if count_a_t == 1000 or count_b_t == 1000:
		count_a = count_a_t
		count_b = count_b_t
		raise Exception("the Connection between the Modules has been severed")
	else:
		count_a = count_a_t
		count_b = count_b_t

	diff = count_b - count_a

	return diff
	