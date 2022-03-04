#length=int(input('enter length:'))
#height=int(input('enter height:'))
#rows = int(input("Enter rows:"))
#cols = int(input("Enter Cols:"))

import math as mt
def Pattern(rows, cols):

	for i in range(1, rows + 1):
		
		
		for j in range(1, i):
			print( end = " ")
		
		
		for j in range(1, cols + 1):

			if (i == 1 or i == rows or
				j == 1 or j == cols):
				print("*", end = "")
			else:
				print(end = " ")
		
		print()


rows, cols = 5, 8


Pattern(rows, cols)


