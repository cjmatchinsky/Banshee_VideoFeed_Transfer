## Banshee_VideoFeed_Transfer
This repository is for the Banshee Video Feed Transfer code:
Raspberry Pi - Receives Video Feed from Ardiuno Via USB connection and processes video feed using CV2 and sends to VPS.
VPS - Receives Video frame and forwards to MEC.
Cloud Computing (MEC) - Recices Video Feed from VPS.


## Connection to Raspberry Pi (rPi) via SSH:
1.  If you need help contact either Cameron, Taila, Don.
2.  Download Advanced ip Scanner (https://www.advanced-ip-scanner.com/).
3.  Open Advanced ip Scanner and make sure the rPi and the computer you are using are on the same WIFI.
4.  EduRom WIFI (school/CPP wifi) will not work.
5.  Use the Advanced ip Scanner to find the IP of the rPi.
6.  Open CMD (Terminal) and enter: SSH pi@123.456.41.240 (the Ip is an example use the ip of the rPi)
7.  When connected it will ask for a password and a yes or no question, hit yes.
8.  The password will be stated in the Banshee Communication Discord.
##
##


## Connection to Virtual private server (VPS) via SSH:
1.  If you need help contact either Cameron, Taila, Don.
2.  Open CMD (Terminal) and enter: SSH root@123.456.41.240 (the IP is an example use the IP of the VPS).
##
##



This is all done through the UDP Socket Server:
1.  Run the VPS code First since it hosts  the server.
2.  Run rPi Code.
3.  Run MEC code. 

Output:
  The video Feed is around 2 FPS

Need more Help and code examples:
https://www.geeksforgeeks.org/sockets-python/#
https://docs.python.org/3/library/socket.html
