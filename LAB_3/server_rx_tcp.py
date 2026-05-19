import socket

# Ascolta su tutte le interfacce
TCP_IP = "172.21.156.96"
TCP_PORT = 48999

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPv4 + TCP
sock.bind((TCP_IP, TCP_PORT))

# Abilita il server ad accettare connessioni (massimo 1 in coda)
sock.listen(1)
print("Server TCP pronto. In attesa di connessione sulla porta %s..." % TCP_PORT)

# Il programma si blocca qui finché il Mac non si connette
conn, addr = sock.accept()
print("Connessione stabilita con il Client:", addr)

count = 0
while True:
    data = conn.recv(1024)
    
    # Se 'data' è vuoto, significa che il client si è disconnesso
    if not data:
        print("Il Client ha chiuso la connessione.")
        break
    
    # TCP POTREBBE UNIRE I PACCHETTI. 
    # Separiamo usando il carattere di terminazione '$'
    messages = data.decode().split("$")
    
    # Cicliamo su tutti i messaggi ricevuti in blocco (escluso l'ultimo vuoto)
    for message in messages[:-1]:
        fields = message.split(",") # Ora separiamo la stringa dal numero di sequenza
        count = count + 1
        print("received message: %s, %s, %d" % (fields[0], fields[1], count))

conn.close()
sock.close()