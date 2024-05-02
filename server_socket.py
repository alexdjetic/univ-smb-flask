import socket

# création d'un socket
serveur_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# address et port d'écoute
adresse = '127.0.0.1'
port = 13002

# liaison su socket au port spécifier
serveur_socket.bind((adresse, port))

# mise en route du serveur
serveur_socket.listen(5)

print("Serveur en attente de connexions...")

# Accepte la connexion entrante
client_socket, client_address = serveur_socket.accept()

print(f"Connexion établie avec {client_address}")

# Reception de données depuis le client
donnees = client_socket.recv(1024).decode()

print(f"Données reçues du client : {donnees}")

# Réponse au client
reponse = "Message reçu par le serveur."
client_socket.send(reponse.encode())

# Fermeture des sockets
client_socket.close()
serveur_socket.close()
