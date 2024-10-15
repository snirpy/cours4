# Boucle for

ports = [22, 80, 443]
for port in ports:
    print(f"Le port {port} est surveillé.")



# Boucle while
compteur = 0
while compteur < 5:
    print(compteur)
    compteur += 1


# Une autre boucle while
temperature = 20
while temperature < 30:
    print(f"Température normale : {temperature}°C")
    temperature += 1  # Simule une augmentation de la température
print("Alerte : Température élevée détectée !")



# Utilisation de break

ip_connexions = ["192.168.1.1", "10.0.0.5", "192.168.1.50"]
ip_suspecte = "192.168.1.50"

for ip in ip_connexions:
    if ip == ip_suspecte:
        print("Alerte : Connexion suspecte détectée !")
        break
    print(f"Connexion depuis {ip} autorisée.")



# Utilisation de continue

logs = ["info: démarrage", "erreur: port fermé", "info: connexion établie"]

for log in logs:
    if "info" in log:
        continue  # Ignore les logs d'information
    print(f"Analyse du log : {log}")


# Boucle for avec range()

for ip_suffix in range(1, 5):
    print(f"Vérification de l'adresse IP : 192.168.1.{ip_suffix}")


# Boucles Imbriquées

ip_list = ["192.168.1.1", "192.168.1.2"]
ports = [22, 80]

for ip in ip_list:
    for port in ports:
        print(f"Vérification du port {port} sur {ip}")

# La Clause else dans les Boucles

connexions = ["SSH", "HTTP", "HTTPS"]
for connexion in connexions:
    print(f"Connexion {connexion} établie.")
else:
    print("Toutes les connexions sont sécurisées.")
