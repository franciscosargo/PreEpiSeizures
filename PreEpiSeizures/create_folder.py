import os

def create_folder():


	nb = input('Type in the patients number : ')
	directory = "/home/Acq_PreEpiSeizures/"+str(nb) + "/"
	#directory = "/home/sargo/Desktop/TESE 2017/Acq_PreEpiSeizures/"+str(nb) + "/"
	
	if not os.path.exists(directory):
		os.makedirs(directory)
		print directory

	return directory