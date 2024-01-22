## Banshee Video Feed (Data Transfer) Code ##

## This code is to access the UDP Socket Server that is hosted on and by the VPS,
## Once the pi and the MEC connect, it will receive frame data from the pi and forward it to the MEC.
## Once the MEC receives the video frame data it will convert it to a usable frame that can be used and viewed by CV2
## For more understanding see the read me file or contact Cameron / Talia. 

import cv2, socket
import numpy as np
import time
import base64

BUFF_SIZE = 65536
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

## This is the IP of the VPS (Put the real IP of the VPS HERE)
#
host_ip = '12.34.56.789'   

## Can Be any port that is not being used.
#
port = 8009    


## This is used to send a message to the VPS so know which IP (or connection to the Server) is the receiver.
#
message = "computer2"
client_socket.sendto(message.encode(),(host_ip, port))


fps, st, frames_to_count, cnt = (0, 0, 20, 0)


while True:

    ## Reviceces Data and Prints Out the frame data and socket number for testing purposes. 
    #
    data, addr1 = client_socket.recvfrom(65536) 
    print(data,addr1)


    ## Converts the received data into the usable frame data that can be viewed.
    #
    data = base64.b64decode(data,' /')
    npdata = np.frombuffer(data,dtype=np.uint8)
    frame = cv2.imdecode(npdata,1)


    ## Shows the Live video frame data with a 0.1 sec delay 
    #
    time.sleep(.1)
    #cv2.imshow("RECEIVING VIDEO",frame)


    ## This is for testing purposes -- This saves the frame data and a JPEG image and then shows the image that was just saved.
    #
    cv2.imwrite("received_fromPI_to_Computer2.jpg", frame)
    time.sleep(.4)
    frame_img = cv2.imread("received_fromPI_to_Computer2.jpg")
    cv2.imshow("RECEIVING VIDEO",frame_img)
    if frame is not None:
        # Save the received frame as a JPEG
        cv2.imwrite("received_frame_TEST.jpg", frame)
    else:
        print('NO save')


    ## Exit the live video stream
    #
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        client_socket.close()
        break


## Ends and closes socket server connection (between MEC and VPS(host) )
#
server_socket.close()
