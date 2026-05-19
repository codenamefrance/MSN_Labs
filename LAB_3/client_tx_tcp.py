import socket
import time

# !!! SOSTITUISCI CON L'IP REALE DEL TUO PC LINUX !!!
UDP_IP = "172.21.156.91" 
UDP_PORT = 47999 
MESSAGE_STRING = "STRINGA" # Scegli una parola a tua scelta (senza spazi) [cite: 57, 74]

print("UDP server IP: %s" % UDP_IP) 
print("UDP destination port: %s" % UDP_PORT)

count = 0 # Contatore dei pacchetti inviati [cite: 77]
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Creazione socket IPv4 + UDP [cite: 79]

while count < 30:
    count = count + 1 
    
    # Composizione del messaggio senza spazi extra: stringa,virgola,sequenza$ [cite: 57, 82]
    message = MESSAGE_STRING + "," + str(count) + "$" 
    print("sending message: %s" % message) 
    
    # Conversione in byte (encode) e invio al server [cite: 62, 83]
    sock.sendto(message.encode(), (UDP_IP, UDP_PORT)) 
    
    time.sleep(0.2) # Attesa obbligatoria di 200 ms [cite: 57, 84]