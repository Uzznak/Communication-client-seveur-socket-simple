import socket

#1
#définir l’adresse IP et le port sur lequel on veut recevoir les données des clients

ADDR = '192.168.10.124'
PORT = 25565 #Le port peut être choisi librement.

#2
# Définir le socket qui nous permettra d’établir une communication avec nos clients
#Note : Socket est point de communication (représenté par une adresse IP suivie d’un port).

#3
# Créer une variable server qui définit le type de socket de notre serveur. 
# pn crée ensuite le socket (socket.socket) 
    #on lui passe 2 arguments fondamentaux.
    # 1 socket.AF_INET = indique qu'on utilise le protocol internet (Internet Protocol, IP)
    # 2 socket.SOCK_STREAM = indique qu'on le protocol TCP pour recevoir et envoyer des données
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#4
# Lier notre adrese IP et notre port au socket
server.bind((ADDR, PORT)) #On passe un tuple avec nos informations

#5
# Paramètrer le serveur pour écouter les communications entrantes et potentiels messages :
#(rappel: server c’est notre socket)

server.listen(5) # nb de connexions autorisées sur le serveur
print(f"[Info] Server started with IP {ADDR} on port {PORT}.")


while True:
    #Code block:
    communication_socket, dest_ip = server.accept() # REF A1
    print(f"[Info] {dest_ip} established a connection to the server.")
#REF A1
#La fonction server.accept() a pour but d’accepter les connexions entrantes à notre socket
   #elle retourne deux variables : le type de socket entrant (communication_socket) et les informations du client (dest_ip)
   #Une fois ces deux variables récupérées, on les affiches pour être informé

#6
#recevoir les potentiels messages des clients :

message = communication_socket.recv(64).decode('utf-8')
print(f"[Message from {dest_ip[0]}:{dest_ip[1]}] {message}")


#On créer une variable message, où on récupère les données envoyées par le socket entrant avec .recv (receive).
    # communication_socket.recv(64) signifie qu’on ne veut revoir que 64bits de données maximum.
    .decode(‘utf-8’) signifie qu’on veut convertir les données envoyées en bits avec l’encoding utf-8 en Unicode, pour qu’elles soient lisibles pour nous.
#En dernière étape on print le message :
#dest_ip retourne par défaut un tuple avec en première position (0) l’adresse IP du client, et en deuxième positions (1) son port.


