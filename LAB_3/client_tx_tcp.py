import socket
import time

# !!! SOSTITUISCI CON L'IP REALE DEL TUO PC LINUX !!!
UDP_IP = "IP_DEL_TUO_PC_LINUX" [cite: 71]
UDP_PORT = 47999 [cite: 73]
MESSAGE_STRING = "STRINGA" # Scegli una parola a tua scelta (senza spazi) [cite: 57, 74]

print("UDP server IP: %s" % UDP_IP) [cite: 75]
print("UDP destination port: %s" % UDP_PORT) [cite: 76]

count = 0 # Contatore dei pacchetti inviati [cite: 77]
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Creazione socket IPv4 + UDP [cite: 79]

while count < 30: [cite: 80]
    count = count + 1 [cite: 81]
    
    # Composizione del messaggio senza spazi extra: stringa,virgola,sequenza$ [cite: 57, 82]
    message = MESSAGE_STRING + "," + str(count) + "$" [cite: 82]
    print("sending message: %s" % message) [cite: 82]
    
    # Conversione in byte (encode) e invio al server [cite: 62, 83]
    sock.sendto(message.encode(), (UDP_IP, UDP_PORT)) [cite: 83]
    
    time.sleep(0.2) # Attesa obbligatoria di 200 ms [cite: 57, 84]