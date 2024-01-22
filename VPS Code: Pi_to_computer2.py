## Banshee Video Feed (Data Transfer) Code ##

## This code is to host the UDP Socket Server on VPS,
## Once the pi and the MEC connect, it will receive frame data from the pi and forward it to the MEC.
## For more understanding see the read me file or contact Cameron / Talia. 


import socket
import numpy as np
import cv2
import base64
import imutils
import time

## VPS server settings
#
HOST = '0.0.0.0'     # Listen on all available network interfaces
PORT = 8009          # Choose an available port number

## Create a socket object
#
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

## Bind the socket to the address and port
#
server_socket.bind((HOST, PORT))


print("Server is listening for incoming connections...")

## The purpose of this look is to wait for the Raspberry Pi and the Cloud Computing (MEC) to be connected to the UDP socket server.
## Once the mec sends the message computer2 it will break the look and start receiving and forwarding the video feed.
#
while(1):
    data, addr1 = server_socket.recvfrom(1024)  
    print(data)
    data=data.decode()

    ## This is used to find out the socket number of the MEC so the VPS knows where to send the frame data.
    #
    if data == "computer2":
        addr_computer2 = addr1
        print(addr_computer2)
        break
        
#print('loop soon')
time.sleep(.01)
while True:
    #print('loop')
    #time.sleep(.1)
    data, addrPI = server_socket.recvfrom(65536)  # You can adjust the buffer size as needed
    print('data_recv')
    message = data
    #time.sleep(.1)
    server_socket.sendto(message, addr_computer2)
    print('data_sent')
    #print(message)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break


server_socket.close()
