def refresh(data, data_socket):
	


	for i in range(0,12):

		if i < 7 :
			data[:-100,i] = data[100:,i]

			data[-100:,i] = data_socket[:,5+i].ravel()
		else : 
			data[:-100,i] = data[100:,i]

			data[-100:,i] = data_socket[:,10+i].ravel()



	return data 	



