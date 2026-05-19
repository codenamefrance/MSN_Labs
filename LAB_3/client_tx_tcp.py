import socket
import time

# !!! SOSTITUISCI CON L'IP REALE DEL TUO PC LINUX !!!
TCP_IP = "172.21.156.91"
TCP_PORT = 48999
MESSAGE_STRING = "TCP_Mac" # Senza spazi

print("Tentativo di connessione al Server TCP IP: %s" % TCP_IP)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPv4 + TCP
sock.connect((TCP_IP, TCP_PORT)) # Handshake iniziale per stabilire la connessione
print("Connesso!")

count = 0
while count < 30:
    count = count + 1
    
    # Formato esatto richiesto: stringa,sequenza$
    message = MESSAGE_STRING + "," + str(count) + "$"
    print("sending message: %s" % message)
    
    sock.send(message.encode()) # In TCP si usa send()
    time.sleep(0.2)

sock.close() # Chiusura elegante della connessione
print("Trasmissione TCP terminata.")