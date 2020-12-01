def broadcast(message, connection, chatroom_clients): 
	for clients in chatroom_clients: 
		if clients!=connection:
			try: 
				print(message)
				clients.send(message.encode('ascii')) 
			except: 
				clients.close() 
				if connection in chatroom_clients: 
					chatroom_clients.remove(connection)

def EnterChatRoom(conn, addr, data, chatroom_clients, username):
	conn.send("Welcome to this chatroom!".encode('ascii')) 
	while True:
		# print("inside try")
		message = conn.recv(2048) #the client in this connection sent a message to be broadcasted
		while(len(message)==0):
			message=conn.recv(2048)
		# print("before if")
		if message:
			print ("<" + username + "> " + message.decode('ascii')) 
			message_to_send = "<" + username + "> " + message.decode('ascii')
			broadcast(message_to_send, conn, chatroom_clients) 

		else: 
			print("Connection broken")
			chatroom_clients.remove(conn)
