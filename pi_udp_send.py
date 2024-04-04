import socket
import cv2
import numpy as np
import time
import imutils
import base64
import os
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.



# Server
HOST = os.getenv("IP")
PORT = int(os.getenv("PORT"))

# UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

vid = cv2.VideoCapture(0)
fps, st, frames_to_count, cnt = (0, 0, 20, 0)

WIDTH = 400

try:
    while True:
        while vid.isOpened():
            ret, frame = vid.read()
            
            frame = imutils.resize(frame, width=WIDTH)
            _, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 80])
            message = base64.b64encode(buffer)
            client_socket.sendto(message, (HOST, PORT))
            # Uncomment the following line if you want to display the frame
            # cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
except Exception as err:
    print(err)
finally:
    vid.release()
    client_socket.close()
