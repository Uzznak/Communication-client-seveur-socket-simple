import socket

#1
TARGET_IP = '192.168.10.124'
TARGET_PORT = 25565

#2
#on définit un socket client 
# arguments : le protocol internet (Internet Protocol et le protocol de transmission TCP.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#3
#connexion au serveur
    #indique à notre socket de se connecter (.connect) à l’IP et au port du serveur (définis dans TARGET_IP et TARGET_PORT).
client.connect((TARGET_IP, TARGET_PORT))
#4 
    #envoi des messages
    #un message au serveur (.sent()) qui contiendra notre input (.input()) qu’on converti en bits avec l’encoding utf-8.
client.send(input().encode('utf-8'))
