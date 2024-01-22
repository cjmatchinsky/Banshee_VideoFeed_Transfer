# Banshee_VideoFeed_Transfer
This repository is for the Banshee Video Feed Transfer code:
Raspberry Pi - Receives Video Feed from Ardiuno Via USB connection and processes video feed using CV2 and sends to VPS.
VPS - Receives Video frame and forwards to MEC.
Cloud Computing (MEC) - Recices Video Feed from VPS.


This is all done through the UDP Socket Server:
1.  Run the VPS code First since it hosts  the server.
2.  Run rPi Code.
3.  Run MEC code. 

Output:
  The video Feed is around 2 FPS

Need more Help and code examples:
https://www.geeksforgeeks.org/sockets-python/#
https://docs.python.org/3/library/socket.html
