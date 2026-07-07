# Mini Projet  (6 et 7 Juillet 2026) 

Le serveur utilise le protocol TCP pour les communications, afin d’assurer la fiabilité des données.
Limite de message recu à 64 bits.


## Technologie utilisée 

- Python ( librarie socket)


# Communication Socket 


## Connexion et envoi de message

On lance le programme du serveur pour le démarrer le serveur, puis le client.

Client démarré avec un input “Hello, World!” prêt à être envoyé

Après avoir écris “Hello, World!”, je presse ENTER pour envoyer le message au serveur, et voyons ce qui se passe :

Le serveur nous a retourné deux informations :
1. Une connexion à été établie avec le client (192.168.10.124:50486, même adresse IP que le serveur car les deux marchent en local, mais le port est évidemment différent)
2. Le message reçu (dans ce cas c'est un monologue dans notre démonstration...)

# Analyse Wireshark

Analysons cette communication dans Wireshark.
