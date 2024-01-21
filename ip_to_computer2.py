import socket
import numpy as np
import cv2
import base64
import imutils
import time

# VPS server settings
HOST = '0.0.0.0'  # Listen on all available network interfaces
PORT = 8009  # Choose an available port number

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the address and port
server_socket.bind((HOST, PORT))

print("Server is listening for incoming connections...")
while(1):
    data, addr1 = server_socket.recvfrom(1024)  # You can adjust the buffer size as needed
    print(data)
    data=data.decode()
    if data == "computer2":
        addr_computer2 = addr1
        print(addr_computer2)
        break
print('loop soon')
time.sleep(.01)
while True:
    print('loop')
    #time.sleep(.1)
    data, addrPI = server_socket.recvfrom(65536)  # You can adjust the buffer size as needed
    print('data_recv')
    message = data
    #time.sleep(.1)
    server_socket.sendto(message, addr_computer2)
    print('data_sent')
    print(message)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break


server_socket.close()