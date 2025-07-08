import socket # Socket module is used for socket programming

server_socket = socket.socket() #To create server socket of ipv4 ip address with TCP protocol

server_socket.bind(("localhost",9999)) # To bind socket with particular ip address & port number

server_socket.listen() # To listen connections from client

print("Waiting for connections....")

while True:
    client_socket, address = server_socket.accept() # To initiates a connection with client, it will return client socket & address of client 
    print("Client Connected ", address)
    
    queryData = client_socket.recv(1024).decode().upper() # To receive data from client & to decode it
    if (queryData == "GOLD"):        
        client_socket.send("49580".encode()) # To send encoded data to client
    else: 
        client_socket.send("Information Not Available".encode()) # To send encoded data to client
        
    queryData = client_socket.recv(1024).decode().upper() # To receive data from client & to decode it
    if (queryData == "SILVER"):        
        client_socket.send("622".encode()) # To send encoded data to client
    else: 
        client_socket.send("Information Not Available".encode())
    
    queryData = client_socket.recv(1024).decode().upper() # To receive data from client & to decode it
    if (queryData == "BRASS"):        
        client_socket.send("4540".encode()) # To send encoded data to client
    else:        
        client_socket.send("Information Not Available".encode()) # To send encoded data to client
    client_socket.close() # To close cpnnection with client    