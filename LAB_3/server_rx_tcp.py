import socket

# "0.0.0.0" indica di ascoltare su tutte le interfacce di rete del PC Linux
UDP_IP = "0.0.0.0" [cite: 86, 88]
UDP_PORT = 47999 [cite: 88]

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Creazione socket IPv4 + UDP [cite: 89]
sock.bind((UDP_IP, UDP_PORT)) # Associazione del socket all'IP e alla porta [cite: 89]

count = 0 # Contatore dei pacchetti ricevuti finora [cite: 60, 90]
print("Server UDP pronto e in ascolto sulla porta %s..." % UDP_PORT)

while True: [cite: 90]
    # Ricezione del pacchetto (buffer impostato a 512 byte come da specifiche) [cite: 61, 91]
    data, addr = sock.recvfrom(512) [cite: 91]
    count = count + 1 [cite: 91]
    
    # Decodifica dei byte in stringa e separazione dei campi tramite la virgola [cite: 63, 92]
    fields = data.decode().split(",") [cite: 92]
    
    # Stampa formattata: stringa, numero di sequenza del pacchetto, conteggio totale [cite: 60, 93]
    print("received message: %s, %s, %d" % (fields[0], fields[1], count)) [cite: 93]