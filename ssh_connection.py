import paramiko

# Détails de connexion
hostname = "192.168.1.102"
port = 22
username = "bnrhm"
password = "saisinbenrhouma"  # Ou utilise une clé privée pour l'authentification sans mot de passe

# Crée un objet SSHClient
client = paramiko.SSHClient()

# Charge les clés du système et accepte automatiquement les clés d'hôtes non connues
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connexion SSH
    print("Tentative de connexion SSH...")
    client.connect(hostname, port, username, password)
    print("Connexion réussie.")

    # Exécuter une commande sur la machine distante
    stdin, stdout, stderr = client.exec_command("hostname")

    # Récupérer la sortie de la commande
    output = stdout.read().decode()
    if output:
        print(f"Sortie de la commande : {output}")
    else:
        print("Aucune sortie reçue de la commande.")
except Exception as e:
    print(f"Erreur de connexion SSH : {e}")
finally:
    # Ferme la connexion
    client.close()
