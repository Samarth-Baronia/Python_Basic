def down_pyramid(n):
	for i in range (1, n + 1):
		for j in range (1, i + 1):
			print (" ", end = "")

		for k in range (n+1 , i, -1):
			print ("*", end = " ")
		print ()

down_pyramid (5)