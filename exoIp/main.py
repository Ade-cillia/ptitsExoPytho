from faker import Faker
import re
import random
import matplotlib.pyplot as plt

fake = Faker()

print("-----------1-----------")

def valider_adresse_ip(ip: str):
  octets = ip.split(".")
  if len(octets) != 4:
    return False
  for octet in octets:
    if int(octet) < 0 or int(octet) > 255:
      return False
  return True


print(valider_adresse_ip("1444.0.0.0"))
print(valider_adresse_ip("144.0.0.0"))
print(valider_adresse_ip("1444.0.0..0"))


print("-----------2-----------")


def convertir_en_binaire(ip: str):
  octets = ip.split(".")
  if len(octets) != 4:
    return False
  for octet in octets:
    if int(octet) < 0 or int(octet) > 255:
      return False
  return ".".join([bin(int(octet))[2:].zfill(8) for octet in octets])

print(convertir_en_binaire("144.0.0.9"))
print(convertir_en_binaire("144.6.0.0"))
print(convertir_en_binaire("150.0.4.0"))



print("-----------3-----------")

def calculer_masque_sous_reseau(nbHosts: int):
  nbUse = 32 - nbHosts.bit_length()
  network_masque_bits = "1" * nbUse + "0" * nbHosts.bit_length()
  network_masque = ""
  for i in range(len(network_masque_bits)):
    network_masque += network_masque_bits[i]
    if (i + 1) % 8 == 0 and i != 31:
      network_masque += "."
  return network_masque

print(calculer_masque_sous_reseau(127))

print("-----------4-----------")
  
def calculer_longueur_prefixe_reseau(ip: str) -> int:
    octets = ip.split(".")
    binaire = "".join([bin(int(octet))[2:].zfill(8) for octet in octets])

    longueur_prefixe = 0
    for bit in binaire:
        if bit == "1":
            longueur_prefixe += 1
        else:
            break

    return int(longueur_prefixe)

program = True

while program:
  print('Entrée une IP (-1 pour arrêter) :')
  ip = input()
  if ip == "-1":
    break
  elif valider_adresse_ip(ip):
    print(f'Entrez le nombre d\'hôtes souhaités (pour l\'IP "{ip}") :')
    notValidHost = True
    while notValidHost:
      nbHosts = input()
      if not nbHosts.isdigit():
        print("Nombre d'hôtes invalide, veuillez entrer un nombre valide.")
        continue
      nbHosts = int(nbHosts)
      max_hosts = 2**(32 - calculer_longueur_prefixe_reseau(ip)) - 2
      if nbHosts > max_hosts:
        print(f"Nombre d'hôtes trop élevé, veuillez entrer un nombre d'hôtes valide.")
        print(f"Pour l'IP {ip}, le nombre d'hôtes maximum est de {max_hosts}.")
        continue
      notValidHost = False
    nbHosts = int(nbHosts)
    network_masque = calculer_masque_sous_reseau(nbHosts)
    ipBinary = convertir_en_binaire(ip)
    nbHostsBinary = bin(nbHosts)[2:].zfill(32 - calculer_longueur_prefixe_reseau(ip))
    nbHostsBinary = '.'.join([nbHostsBinary[i:i+8] for i in range(0, len(nbHostsBinary), 8)])
    print(f"IP                       : {ip}")
    print(f"Nombre d'Hôte            : {nbHosts}")
    print(f"IP en Binaire            : {ipBinary}")
    print(f"Nombre d'Hôte en Binaire : {nbHostsBinary}")
    print(f"Masque de sous-réseau    : {network_masque}")
  else:
    print(f"IP : {ip} invalide, veuillez entrer une IP valide.")
