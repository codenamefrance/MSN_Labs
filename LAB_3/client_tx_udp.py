# client_tx.py (ex server.py)
import socket
import time

UDP_IP = "172.21.156.91" # Questo deve essere l'IP del ricevitore (il tuo Mac)
UDP_PORT = 48000
MESSAGE_STRING = "STRINGA"

print("UDP target IP: %s" %UDP_IP)
print("UDP target port: %s" %UDP_PORT)

count = 0 # Counter to count the number of packets
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # IPv4 + UDP [cite: 79]

while count < 30:
    count = count + 1
    # Rimossi gli spazi extra per rispettare la formattazione richiesta
    message = MESSAGE_STRING + "," + str(count) + "$" 
    print("sending message: %s" % message)
    sock.sendto(message.encode(), (UDP_IP, UDP_PORT)) # [cite: 83]
    time.sleep(0.2) # Wait 200 ms before sending the next packet [cite: 84]