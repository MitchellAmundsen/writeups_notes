from socket import create_connection

conn = create_connection(('localhost', 1337))
conn.recv(1000) # get up to 1000 bytes, or an endline
conn.send(bytes("Stuff stuff stuff."))
conn.close() # not required