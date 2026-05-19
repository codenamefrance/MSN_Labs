# server_rx.py (ex client.py)
import socket

UDP_IP = "172.22.156.57" # IP dell'interfaccia di ricezione (Mac) 
UDP_PORT = 47999

# Corretto l'errore di sintassi su SOCK_DGRAM
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # IPv4 + UDP 
sock.bind((UDP_IP, UDP_PORT)) # 

count = 0 # To count the number of packets received so far

while True:
    data, addr = sock.recvfrom(512) # data contains the packet payload [cite: 91]
    count = count + 1
    # Corretto lo split per non cercare spazi inesistenti
    fields = data.decode().split(",") # 
    # Sistemata un po' la formattazione del print
    print("received message: %s, %s, %d" % (fields[0], fields[1], count)) # [cite: 93]