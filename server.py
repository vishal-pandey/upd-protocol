import socket

localIP = "127.0.0.1"
localport = 20001
buffersize = 1024

msgFromServer = "Hello From Server"
bytesToSend = str.encode(msgFromServer)

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type = socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localport))

print("UDP Server up and listening")


# listen for incoming datagram

while ( True ):
	bytesAddressPair = UDPServerSocket.recvfrom(buffersize)
	message = bytesAddressPair[0]
	address = bytesAddressPair[1]

	clientMsg = "Message from Client:{}".format(message)
	clientIP = "Client IP Address:{}".format(address)

	print(clientMsg)
	print(clientIP)

	# Sending a reply to client

	UDPServerSocket.sendto(bytesToSend, address)
