import socket

# création du socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serveur_adresse = '127.0.0.1'
serveur_port = 13002

# connexcion au serveur
client_socket.connect((serveur_adresse, serveur_port))

# envoie du message
message = "Bonjour, serveur!"
client_socket.send(message.encode())

# reception de la réponse du serveur
reponse = client_socket.recv(1024).decode()

# fermeture du socket
client_socket.close()
