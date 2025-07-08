import socket # Socket module is used for socket programming

client_socket = socket.socket() # To create client socket

client_socket.connect(("localhost",9999)) # To connect server machine , mention server ip address & port number

client_socket.send("gold".encode()) # To send encoded data to server
print("10g Gold   Rs=> {0}".format(client_socket.recv(1024).decode())) # To receive data from server & to decode it

client_socket.send("Silver".encode()) # To send encoded data to server
print("10g Silver Rs=> {0}".format(client_socket.recv(1024).decode())) # To receive data from server & to decode it

client_socket.send("brass".encode()) # To send encoded data to server
print("10Kg Brass Rs=> {0}".format(client_socket.recv(1024).decode())) # To receive data from server & to decode it
client_socket.close() # To close connection