from socket import create_connection

conn = create_connection(('fastmaze.mitctf.com', 4373)) 
#conn.recv(1000) # get up to 1000 bytes, or an endline
#conn.send(bytes("Stuff stuff stuff."))
#conn.close() # not required


for i in range(10):
	arr = []
	for i in range (6):
		data = conn.recv(1000)
		#print data
		lines = data.splitlines()
		for line in lines:
			arr.append(line)
		print arr		


'''
for i in range(7):
	print conn.recv(1000)
	print '---------------'
'''
'''
append = False
for i in range(10):
	arr = []
	data1 = conn.recv(1000)
	print data1
	data2 = conn.recv(1000)
	print data2
	data2.splitlines()	
	count = 0
	while(data2[count][0] != '#'):
		count = count + 1
	while(len(arr) >  count):
		arr.append(data2[count])
		count = count + 1
	print arr
	data3 = conn.recv(1000)
	count3 = 0
	while(data3[count3][0] != 'Y'):
		arr.append(data3[count3])
		count3 = count3 + 1
	print arr 

'''



