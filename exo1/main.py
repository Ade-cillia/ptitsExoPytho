from faker import Faker
import re
import random
import matplotlib.pyplot as plt

fake = Faker()

def generate_packet():
    randomEmail = ""
    if bool(random.getrandbits(1)):
      randomEmail = fake.email()
    else:
      randomEmail = "dsbdj@dsqk@ds."
    packet = {
        "username": fake.user_name(),
        "ip_address": fake.ipv4(),
        "email": randomEmail,
        "country": fake.country(),
    }
    return packet

def filterPacketsIpStartWith(packets, ipStart):
    filterPacket = []
    for packet in packets:
        if packet['ip_address'].startswith(ipStart):
            filterPacket.append(packet)
    return filterPacket

def verifEmail(email: str):
  regex = r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
  if re.search(regex, email):
      return True
  return False

def getDomainFromEmail(dictionary):
  return

packets = [generate_packet() for _ in range(100)]

# Filter Ip Start With
filtered_packets = filterPacketsIpStartWith(packets, '170')
for packet in filtered_packets:
    print(packet)

print("----------------------")

# Sort by Username
packetsSortByUsername = packets
packetsSortByUsername.sort(key= lambda a: a["username"])
for packet in packetsSortByUsername:
    print(packet)

print("----------------------")

# Test Email
invalidEmail = 0
for packet in packets:
  isValid = verifEmail(packet["email"])
  txt = ""
  if(not isValid):
    txt = "Email invalide pour: {}".format(packet)
    print(txt)
    invalidEmail+=1
result = "Il y a donc eu {} email(s) invalide(s)"
print(result.format(invalidEmail))

print("----------------------")


#add ducplicate data for test
packets.append(packets[0])

seen = set()
unique_packets = []
duplicate_count = 0

for packet in packets:
    packet_tuple = tuple(packet.items())
    if packet_tuple not in seen:
        seen.add(packet_tuple)
        unique_packets.append(packet)
    else:
        duplicate_count += 1

packets = unique_packets

print(packets)
print(f"{duplicate_count} data were removed as duplicates")


print("----------------------")
# Get domain from url
for packet in packets:
  print(f"{packet} -> domain : {packet['email'].split('@')[1]}")


print("----------------------")
# Graph
data = {}
for packet in packets:
    country = packet["country"]
    if country in data:
        data[country] += 1
    else:
        data[country] = 1


filtered_data = {key: value for key, value in data.items() if value >=1}

# initials_data = {key[:2]: value for key, value in filtered_data.items()}

fig = plt.figure(figsize=(20, 10))

plt.bar(list(filtered_data.keys()), list(filtered_data.values()))
plt.xlabel("Country Initial")
plt.ylabel("Number of IP addresses")
plt.title("Number of IP addresses per Country Initial (>1 IP)")
plt.grid(True)

# Rotate x-axis labels vertically
plt.xticks(rotation='vertical')
plt.show()
