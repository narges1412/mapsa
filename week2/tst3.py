
locmin=0
locmax=0

def MaximaMinima(n, arr):

	
	mx = []
	mn = []

	
	

	
	for i in range(1, n-1):

		
		if(arr[i-1] > arr[i] < arr[i + 1]):
			mn.append(i)

		
		elif(arr[i-1] < arr[i] > arr[i + 1]):
			mx.append(i)

	
	

		
	if(len(mx) > 0):
		print("Local maxima"\
			" are : ", end ='')
		print(*mx)
        
	else:
		print(" points of"\
			" Local maxima.")

	if(len(mn) > 0):
		print("Points of Local minima"\
			" are : ", end ='')
		print(*mn)
        
	else:
		print("There are no points"\
			" of Local minima.")

#


	n= 9
	# 
	arr = [11,8,12,9,1,5,12,21,3,4,9,2,5]

	
	MaximaMinima(N, arr)
