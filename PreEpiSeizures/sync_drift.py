
from find_sync import *

def sync_drift(t, count_a, count_b):
	a_I1 = t[0:,2]
	b_I1 = t[0:,12]
	count_a_t = find_sync(a_I1)
	count_b_t = find_sync(b_I1)

	if count_a_t == 1000 or count_b_t == 1000:
		flag_sync = 1
		count_a = count_a + count_a_t
		count_b = count_b + count_b_t
		raise Exception("the Connection between the Modules has been severed")
	else:
		flag_sync = 0
		count_a = count_a + count_a_t
		count_b = count_b + count_b_t

	diff = count_b - count_a
	return diff, count_a, count_b
	